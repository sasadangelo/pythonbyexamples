import os
import sys

# This is how to define a function in Python.
# There is no standard main function in Python.
# Call it "main" is just a convention.
def main():
    print(f"Hello {sys.argv[0]} !!!")

# This is a comment
# Standard boilerplate to call the main() function to begin # the program.
# In Python there is no concept of main function. This is a way to simulate it
# and process arguments
if __name__ == '__main__':
    main()
