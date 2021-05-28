# This example shows how to use if.
num=6
if num%2==0:
    print(f"{num} is an even number.")

# This example shows how to use if/else.
num=5
if num%2==0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# This example shows how to use if/elif/else.
# You can use operators like: >, <, >=, <=, !=, ==, is, in
num=4
if num>=0 and num<4:
    print(f"{num} is a small number.")
elif num>=4 and num<8:
    print(f"{num} is a medium number.")
else:
    print(f"{num} is a big number.")
