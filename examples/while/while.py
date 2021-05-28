letters=['a','b','c','d']

# While loops through the list, element by element, and print it.
# len      --> return the list length
# end =" " --> print without new line
i=0
while i<len(letters):
    print(letters[i], end =" ")
    i+=1

# Print a new line
print()

# While infinite loop to print the first 5 numbers. The instruction break
# is used to exit from the loop.
i=0
while True:
    if i==5:
        break
    print(i, end =" ")
    i+=1

# Print a new line
print()

# Use while loop to print all the numbers in [0,10) but 5.
# We use the continue statement.
i=0
while i<10:
    if i==5:
        i+=1
        continue
    print(i, end =" ")
    i+=1

# Print a new line
print()
