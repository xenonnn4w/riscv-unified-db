import yaml
import pprint
import sys
import os

# Step1: Read the YAML file 
if len(sys.argv) > 1:
    yaml_file = sys.argv[1]
else:
    yaml_file = 'spec/std/isa/inst/mock.yaml'

with open(yaml_file, 'r') as f:
    data = yaml.safe_load(f)

# Step2: Print the parsed data 
print(f'Parsed YAML data from {yaml_file}:')
pprint.pprint(data)

# Step3: Generate a C header file from the YAML data
if len(sys.argv) > 2:
    header_base = sys.argv[2]
else:
    header_base = os.path.splitext(os.path.basename(yaml_file))[0]

header_filename = header_base + '.h'

# Helper: sanitize C string
def c_str(s):
    return s.replace('"', '\"').replace('\n', ' ')

with open(header_filename, 'w') as h:
    h.write('// Auto-generated from {}\n'.format(yaml_file))
    h.write(f'#ifndef {header_base.upper()}_H\n#define {header_base.upper()}_H\n\n')
    h.write('#include <stdbool.h>\n\n')
    # macros
    h.write(f'#define INST_NAME "{c_str(data["name"])}"\n')
    h.write(f'#define INST_LONG_NAME "{c_str(data["long_name"])}"\n')
    h.write(f'#define INST_DESCRIPTION "{c_str(data["description"])}"\n')
    h.write(f'#define INST_ASSEMBLY "{c_str(data["assembly"])}"\n')
    h.write(f'#define INST_ENCODING_MATCH "{c_str(data["encoding"]["match"])}"\n')
    h.write(f'#define INST_DATA_INDEP_TIMING {str(data.get("data_independent_timing", False)).lower()}\n')
    # Access struct
    h.write('typedef struct {\n')
    for k in ['s', 'u', 'vs', 'vu']:
        h.write(f'    bool {k};\n')
    h.write('} inst_access_t;\n\n')
    h.write('static const inst_access_t inst_access = {\n')
    for k in ['s', 'u', 'vs', 'vu']:
        v = data['access'].get(k, 'never')
        h.write(f'    .{k} = {str(v == "always").lower()},\n')
    h.write('};\n\n')
    # Encoding variables
    h.write('typedef struct {\n    const char* name;\n    const char* location;\n} inst_var_t;\n\n')
    h.write(f'static const inst_var_t inst_encoding_vars[{len(data["encoding"].get("variables", []))}] = {{\n')
    for var in data['encoding'].get('variables', []):
        h.write(f'    {{ "{c_str(var["name"])}", "{c_str(var["location"])}" }},\n')
    h.write('};\n\n')
    h.write(f'#endif // {header_base.upper()}_H\n')
print(f"C header file '{header_filename}' generated from {yaml_file}.") 