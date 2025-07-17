#include <stdio.h>
#include "inst_mock_out.h"

int main(void) {
    printf("name: %s\n", INST_NAME);
    printf("long_name: %s\n", INST_LONG_NAME);
    printf("description: \"%s\"\n", INST_DESCRIPTION);
    printf("assembly: %s\n", INST_ASSEMBLY);
    printf("encoding:\n");
    printf("  match: %s\n", INST_ENCODING_MATCH);
    printf("  variables:\n");
    for (size_t i = 0; i < sizeof(inst_encoding_vars)/sizeof(inst_encoding_vars[0]); ++i) {
        printf("    - name: %s\n", inst_encoding_vars[i].name);
        printf("      location: %s\n", inst_encoding_vars[i].location);
    }
    printf("access:\n");
    printf("  s: %s\n", inst_access.s ? "always" : "never");
    printf("  u: %s\n", inst_access.u ? "always" : "never");
    printf("  vs: %s\n", inst_access.vs ? "always" : "never");
    printf("  vu: %s\n", inst_access.vu ? "always" : "never");
    printf("data_independent_timing: %s\n", INST_DATA_INDEP_TIMING ? "true" : "false");
    return 0;
} 