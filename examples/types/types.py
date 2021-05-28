import os
import sys

def main():
    # Python is a stricty typed programming language.
    # However, there is no need to declare the variable type.
    # Python understand it from code.
    a=1
    b=2*a
    # By default, numbers are considered int unless you do not give
    # additional info to Python to understand its type.
    # In this case c is a float.
    c=3.0
    # String single line. In Python you can use single or double quotes.
    d='kkkk'
    e="kkkk"
    # String multi line. In Python it is possible to define string variables multi lines.
    f='''aaaaa
bbbbb
ccccc'''
    # multi assignment
    g = h = a
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))
    print(f, type(f))
    print(g, type(g))
    print(h, type(h))

    # Primitive types in Python are immutable.
    # Python doesn't allocate space for variable a. In Python
    # variables, even though they reference a primitive type,
    # is a reference. In the example below, Python allocate a space
    # where it outs the value 1 and a reference to this area.
    # This area referenced is immutable and cannot change. If I assign
    # to a another value (i.e. 2) there will be another area and simply a will

# Standard boilerplate to call the main() function to begin # the program.
if __name__ == '__main__':
    main()
