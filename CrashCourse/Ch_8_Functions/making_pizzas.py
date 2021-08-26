# Tell Python to open the file pizza.py and copy all the functions from it
#  into this program.
import pizza

# Each function in the module is available with the following syntax:
#  module_name.function_name()
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# General syntax for mporting a specific function from a module
#  from module_name import function_name
# Can import as many functions as you want
#  from moduke_name import function_0, function_1, function_2

from pizza import make_pizza

make_pizza(18, 'pepperoni')
make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')

# Don't need the dot notation because the function is explicitly imported

# An alias can be used if importing functions causes issues with existing names

from pizza import make_pizza as mp
mp(20, 'pepperoni')
mp(16, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax to use an alias is:
#  from module_name import function_name as fn

# Can also provide an alias fro a module name
import pizza as p

p.make_pizza(22, 'pepperoni')
p.make_pizza(18, 'mushrooms', 'green peppers', 'extra cheese')

# The general syntax for this approach is:
#  import module_name as mn

from pizza import * # Imports every function in module
make_pizza(24, 'pepperoni')
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')

# This method is not encouraged with larger modules that I didn't write. Syntax:
#  from module_name import *