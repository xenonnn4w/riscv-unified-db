# typed: true

# DO NOT EDIT MANUALLY
# This is an autogenerated file for types exported from the `bigdecimal` gem.
# Please instead update this file by running `bin/tapioca gem bigdecimal`.


# source://bigdecimal//lib/bigdecimal/util.rb#78
class BigDecimal < ::Numeric
  # source://bigdecimal//lib/bigdecimal/util.rb#110
  def to_d; end

  # source://bigdecimal//lib/bigdecimal/util.rb#90
  def to_digits; end
end

BigDecimal::VERSION = T.let(T.unsafe(nil), String)

# source://bigdecimal//lib/bigdecimal/util.rb#138
class Complex < ::Numeric
  # source://bigdecimal//lib/bigdecimal/util.rb#157
  def to_d(*args); end
end

# source://bigdecimal//lib/bigdecimal/util.rb#171
class NilClass
  include ::Treetop::Compiler::Metagrammar::LabeledExpressionSequenceBody0

  # source://bigdecimal//lib/bigdecimal/util.rb#182
  def to_d; end
end
