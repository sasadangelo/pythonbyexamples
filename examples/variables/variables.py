# Python is a stricty typed programming language.
# However, there is no need to declare the variable type.
# Python understand it from code.
a=1
b=2*a

# By default, numbers are considered int unless you do not give
# additional info to Python to understand its type.
# In this case c is a float.
c=3.0
d=7.0/3.0

# String single line. In Python you can use single or double quotes.
e='This is a single quote string'
f="This is a double quote string"

# String multi line. In Python it is possible to define string variables multi lines.
g='''aaaaa
bbbbb
ccccc'''

# Multi assignment
h = i = a

# Print variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# Primitive types in Python are immutable.
# Python doesn't allocate space for a variable. In Python
# variables, even if they reference a primitive type,
# is a reference. In the example above, Python allocate a space
# where it store the value and the variable is only a label that referencea it.
# This area referenced is immutable and cannot change. If I assign
# to the variable another value, it will be stored in another area and the variable
# will reference it.
