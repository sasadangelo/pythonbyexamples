# Tuples are immutable sequences of heterogeneous elements.
# Tuples are iterables.
print("---- heterogeneous tuples")
tuple=('a',1,'myelement',5.0)
print(tuple)

# You can use operator [] to referent list elements.
# First element has index 0.
# Index -1 is the last element.
# You can declare tuple without ()
print("---- operator []")
tuple=1,2,3,4,5,6,7,8,9,10
print("tuple =", tuple)
print("tuple[0] =", tuple[0])
print("tuple[5] =", tuple[5])
print("tuple[-1] =", tuple[-1])
print("tuple[-2] =", tuple[-2])

# Tuple can be empty.
print("---- empty tuple")
tuple=()
print(tuple)

# Tuples can be sliced. Slice is a copy of the whole tuple (i.e. tuple[:]) or
# a part of it tuple[i:j]
# tuple[2:5] means list from index 2 to 5-1
print("---- tuple sliced")
tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple)
print("tuple[2:5] =", tuple[2:5])
print("tuple[:] =", tuple[:])

# You can use the following functions with the lists:
# - sum
# - len
# - index, return the index of specified value
# - count
print("---- functions sum, len, etc.")
tuple=(1,5,8,10)
print("tuple =", tuple)
print("sum =", sum(tuple))
print("len =", len(tuple))
print("index(5) =", tuple.index(5))
# count function returns the number of occurrences of the argument
print("count(10) =", tuple.count(10))

# You can use + and * operators with tuples
print("---- operator + and *")
tuple=(1,2,3,4,5,6,7,8,9,10)
print("tuple =", tuple)
print("tuple+(1,2) =", tuple+(1,2))
print("tuple*2 =", tuple*2)

# List are iterable
print("---- tuple iterables")
tuple=(1,5,8,10)
print("tuple =", tuple)
for e in tuple:
    print(e, end=" ")
else:
    print()

# Tuple are enumerable
print("---- enumerate tuple")
tuple=(1,5,8,10)
print("tuple =", tuple)
for i, e in enumerate(tuple):
    print(i,"=",e)
