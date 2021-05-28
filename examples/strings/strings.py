# You can use " or ' to declare strings.
print("---- definitions")
s1="Double quote string"
s2="Single quote string"
print("s1 =", s1)
print("s2 =", s2)

# You can use operator [] to referent list elements.
# First element has index 0.
# Index -1 is the last element.
# You can declare tuple without ()
print("---- operator []")
s="Double quote string"
print("s =", s)
print("s[0] =", s[0])
print("s[5] =", s[5])
print("s[-1] =", s[-1])
print("s[-2] =", s[-2])

# Striong can be empty.
print("---- empty string")
print("")

# Strings can be sliced. Slice is a copy of the whole string (i.e. string[:]) or
# a part of it string[i:j]
# string[2:5] means string from index 2 to 5-1
print("---- string sliced")
s="Double quote string"
print(s)
print("s[2:5] =", s[2:5])
print("s[:] =", s[:])

# You can use the following functions with the lists:
# - find
# - split
# - index, return the index of specified value
# - strip, lstrip, rstrip
# - upper
# - lower
# - count
# - replace
# - startswith
# - endswith
print("---- functions find, split, etc.")
s=" Double quote string "
print("find('quo') =", s.find('quo')) # find substring
print("split(' ') =", s.split(' '))   # tokenize the string using input character, return a list
print("index('u') =", s.index('u'))   # similar to find
print("strip() =", s.strip())         # strip spaces on left and right, you can use different chars in input
                                      # lstrip, strip on the left
                                      # rstrip, strip on the right
print("upper() =", s.upper())         # convert string in upper case
print("lower() =", s.lower())         # convert string in lower case
# count function returns the number of occurrences of the argument
print("count('u') =", s.count('u'))
print("replace('Double','Single') =", s.replace('Double','Single'))
print("startswith('Double') =", s.startswith('Double'))
print("endswith('string ') =", s.endswith('string '))

# You can use + and * operators with tuples
print("---- operator + and *")
s='String'
print("s =", s)
print("s + ' new' =", s + ' new')
print("s * 2 =", s*2)

# List are iterable
print("---- string iterables")
s='String'
print("s =", s)
for c in s:
    print(c, end=" ")
else:
    print()

# Tuple are enumerable
print("---- enumerate string")
s='String'
print("s =", s)
for i, c in enumerate(s):
    print(i,"=",c)

