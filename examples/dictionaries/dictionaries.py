# Dictionaries are collections of key/value pairs. Dictionary is a mutable collection but Keys are immutable.
# You can  create a dictionary like this.
print("---- create dictionaries")
my_dict1 = {1: 'apple', 2: 'ball'}
my_dict2 = dict({1:'apple', 2:'ball'})
print("my_dict1 =", my_dict1)
print("my_dict2 =", my_dict2)

# Create an empty dictionary.
print("---- create empty dictionary")
my_dict = {}
print("my_dict =", my_dict)

# Dictionary can contains mixed type keys.
print("---- Mixed type keys dictionary")
my_dict = {'name': 'John', 1: [2, 4, 3]}
print("my_dict =", my_dict)

# Create dictionary from a list of key/value tuples.
print("---- Create dictionary from a list of key/value tuples")
my_dict = dict([(1,'apple'), (2,'ball')])
print("my_dict =", my_dict)

# User operator [] and function get() to get value from a key.
# User operator [] to set value for a key.
# The difference between [] and get() is that if key doesn't exist the [] throw an exception,
# get will return None.
print("---- Get/Set value")
my_dict = {1: 'apple', 2: 'ball'}
print("my_dict[1] =", my_dict[1])         # get key with operator []
print("my_dict.get(2) =", my_dict.get(2)) # get key
print("my_dict.get(3) =", my_dict.get(3)) # get not existing key
my_dict[1]='banana'                       # update the value of key 1
print("my_dict =", my_dict)
my_dict[3]='cherry'                        # add a new key/value
print("my_dict =", my_dict)

# Use some useful dictionary functions.
# - keys, return all dictionary keys
# - values, return all dictionary values
# - copy, return a dictionary copy
# - pop, remove an item and return it
# - update, update a key/value
# - len
# - clear, remove all key/value
print("---- Dictionary functions")
my_dict = {1: 'apple', 2: 'ball', 3: 'cherry'}
print("my_dict.keys =", my_dict.keys())
print("my_dict.values =", my_dict.values())
my_dict_copy = my_dict.copy()
print("my_dict_copy =", my_dict_copy)
print("my_dict_copy.pop(1) =", my_dict_copy.pop(1))
print("my_dict_copy =", my_dict_copy)
banana = {2: 'banana'}
my_dict_copy.update(banana)
print("my_dict_copy =", my_dict_copy)
print("len(my_dict_copy) =", len(my_dict_copy))
my_dict_copy.clear()
print("my_dict_copy =", my_dict_copy)

# Dictionary are iterable on keys or values
print("---- Dictionary iteration")
my_dict = {1: 'apple', 2: 'ball', 3: 'cherry'}
for k in my_dict.keys():
    print(k, my_dict[k])

# Dictionaries are not sliceable. If you want only a
# subset of the dictionary containing only a subset of key
# you need to create it by yourself.
