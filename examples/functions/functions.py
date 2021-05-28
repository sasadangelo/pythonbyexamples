#This function simply print the message "Hello Function !!!"
def hello_func():
    print("Hello Function !!!")

# A function can take in input one or more parameters. It is not
# necessary specify their type, because Python infer them from
# the arguments passed.
def hello_msgs(msg1, msg2):
    print(msg1, msg2)

# Python functions support default parameter values.
# Basically, you can specify a default value for a parameter and if
# it is called without passing any value for it, the default value is considered.
# This is the first way to support function with a variable number of arguments.
def hello_default(msg1='Hello', msg2='Default !!!'):
    print(msg1, msg2)

# There is another way to use function with variable number of arguments.
# In this case we are going to use an iterable object.
def hello_args(*args):
    for arg in args:
        print(arg, end=" ")
    else:
        print()

# === Main function ===

# Call the hello_func function.
hello_func()

# The parameters are assigned to the arguments by position.
hello_msgs("Hello", "Function !!!")

# If the argument name is specified, you can pass them in any order.
hello_msgs(msg2="Function !!!", msg1="Hello")

# No argument is passed for msg2, in this case the default value is used.
hello_default(msg1='Hi')

# In this example, we pass a variable number of argument of any type
hello_args('Hi', 'from', 'hello_args', 'function (', 1, ')')
