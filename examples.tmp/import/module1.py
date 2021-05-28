# From module "module" import only function f
from module import f

if __name__ == '__main__':
    # Now you can call f without specify the identifier "module"
    print(f(5))
