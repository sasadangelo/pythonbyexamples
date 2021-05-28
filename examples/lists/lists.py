# Lists are mutable sequences of heterogeneous elements
print("---- heterogeneous list")
list=['a',1,'myelement',5.0]
print(list)

# You can use operator [] to referent list elements.
# First element has index 0.
# Index -1 is the last element.
print("---- operator []")
list=[1,2,3,4,5,6,7,8,9,10]
print("list[0] =", list[0])
print("list[5] =", list[5])
print("list[-1] =", list[-1])
print("list[-2] =", list[-2])

# List can be empty.
print("---- empty list")
print([])

# Lists can be sliced. Slice is a copy of the whole list (i.e. list[:]) or
# a part of it list[i:j]
# list[2:5] means list from index 2 to 5-1
print("---- list sliced")
list=[1,2,3,4,5,6,7,8,9,10]
print(list[2:5])
print(list[:])

# You can use the following functions with the lists:
# - sum
# - len
# - append
# - insert
# - index
# - remove
# - sort
# - reverse
# - count
# - pop
# - extend
print("---- functions sum, len, etc.")
list=[1,5,8,10]
print("sum =", sum(list))
print("len =", len(list))
list.append(2)
print("after append =", list)
list.insert(2, 4)
print("after insert =", list)
print("index of 5 =", list.index(5))
list.remove(5)
print("after remove(5) =", list)
list.sort()
print("after sort =", list)
list.reverse()
print("after reverse =", list)
# count function returns the number of occurrences of the argument
print("count(10) =", list.count(10))
# pop functions can be used to implement FIFO/LIFO
print("pop(0) =", list.pop(0)) # useful for FIFO
print(list)
print("pop(-1) =", list.pop(-1)) # useful for LIFO
print(list)
# entend list with another list
list.extend([4,9])
print("extend([4,9]) =", list)

# List are iterable
print("---- list iterables")
list=[1,5,8,10]
print(list)
for e in list:
    print(e, end=" ")
else:
    print()

# List are enumerable
print("---- enumerate list")
list=[1,5,8,10]
print(list)
for i, e in enumerate(list):
    print(i,"=",e)

# Join of list of characters
print("---- join")
list=['S','t','r','i','n','g']
print("".join(list))
