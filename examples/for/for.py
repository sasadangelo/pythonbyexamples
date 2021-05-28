letters=['a','b','c','d']

# For loops through the list, element by element, and print it.
# end =" " --> print without new line
for s in letters:
    print(s, end =" ")

# Print a new line
print()

# The enumerate function return two value:
# - the index of the element
# - the element
for i, s in enumerate(letters):
    print(i, s)

# range is a generator function that return the list
# [0, 1, 2, 3, 4]
# in this example, the for loops through it
for i in range(5):
    print(i, end =" ")

# Print a new line
print()

# The function range can start from any number. For example,
# range(5, 10)=[5, 6, 7, 8, 9]
for i in range(5,10):
    print(i, end =" ")

# Print a new line
print()

# The function range, by default, increment by 1 but you
# can skip by any number. For example:
# range(0,10,2)=[0,2,4,6,8]
for i in range(0,10,2):
    print(i, end =" ")

# Print a new line
print()

# You can use continue in for loop like in C.
# It run the next for loop.
for i in range(5):
    if (i%2==0):
       print(f"{i} is an even number.")
    else:
       continue

# You can use else with for loop. It
# will be executed at the end of the loop.
for i in range(5):
    print(i, end =" ")
else:
    print("end loop")

# This example prints the numbers: 0, 1, 2, 3, 4.
# When i==5 it breaks and the else clause is not run.
# A rule of the for loop is that if break is executed
# the else clause is not run.
# It run the next for loop.
for i in range(10):
    if (i==5):
       break
    else:
        print(i, end =" ")
else:
    print("end loop")
