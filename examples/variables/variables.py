# Python is a stricty typed programming language.
# However, there is no need to declare the variable type,
# Python understand it from code.
a=1
b=2*a

# By default, numbers are considered int unless you do not give
# additional info to Python to understand its type.
# In this case c is a float.
c=3.0
d=7.0/3.0

# To declare strings in Python you can use single or double quotes interchangeably.
e='This is a single quote string'
f="This is a double quote string"

# In Python it is possible to declare multi line strings.
g='''aaaaa
bbbbb
ccccc'''

# Python supports multi assignment.
h = i = a

# Print variables.
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
# Python doesn't allocate space for a variable, it simply
# reference the area containing the value. This value cannot change.
# If you assign to the variable another value, it simply refers to another
# memory location.
