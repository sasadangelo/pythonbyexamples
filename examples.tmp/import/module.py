# Here I define the function f in the module "module"
# A module is a namespace where you can define objects like
# variables, functions, objects that can be used by callers.
a=1
_a=2

def g(x):
    return x+2

def f(x):
    return x+1

if __name__ == '__main__':
    print(f(3))
