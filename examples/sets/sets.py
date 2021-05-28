# Sets are collections of unordered, not indexable, not duplicable values. A Set is  mutable.
# You can  create a dictionary like this.
print("---- create sets")
my_set1 = {'apple', 'banana', 'cherry'}
my_set2 = set({'apple', 'banana', 'cherry'})
print("my_set1 =", my_set1)
print("my_set2 =", my_set2)

# Create an empty set.
print("---- create empty set")
my_set = {}
print("my_set =", my_set)

# Set can contains mixed type keys.
print("---- Mixed type set")
my_set = {'apple', 'banana', 'cherry', 1}
print("my_set =", my_set)

# Create dictionary from a list of key/value tuples.
print("---- Create dictionary from a list of key/value tuples")
my_set = set(['apple', 'banana', 'cherry', 1])
print("my_set =", my_set)

# Use some useful dictionary functions.
# - add, add an element to the set
# - copy, return a dictionary copy
# - pop, remove an item and return it
# - update, update one or more values
# - len
# - union
# - discard, remove, remove an element from the set. The difference is
#                    that remove raise an exception is an element is not
#                    found, while discard return None.
# - clear, remove all key/value
print("---- Dictionary functions")
my_set = {'apple', 'banana', 'cherry', 1}
my_set.add('kiwi')
print("my_set.add('kiwi') =", my_set)
my_set.update(['orange','pear'])
print("my_set.update(['orange','pear']) =", my_set)
my_set_copy = my_set.copy()
print("my_set_copy =", my_set_copy)
print("my_set.pop() =", my_set.pop()) # sets are unordered, so you don't know which element is pop
print("my_set =", my_set)
print("len(my_set) =", len(my_set))
my_set1={1, 2, 3}
print("my_set.union(my_set1) =", my_set.union(my_set1)) # union return the union set, but it does not change the original set
my_set.discard(1)
print("my_set =", my_set)
my_set.clear()
print("my_set =", my_set)

# There are other functions like:
# - difference
# - difference_update
# - intersection
# - intersection_update
# - isdisjoint
# - issubset
# - issuperset
# - symmetric_difference
# - symmetric_difference_update

# Set are iterable
print("---- Set iteration")
my_set = {'apple', 'banana', 'cherry', 1}
for e in my_set:
    print(e)

# Sets are not sliceable. If you want only a
# subset of the dictionary containing only a subset of key
# you need to create it by yourself.
