# comments look like this
# variables, data types
a = 3 # this is an integer
b = 8.5 # this is a float

print(type(a), type(b), a, b)

print(a+b, a/b, b/a, b**a)

print(b//a, b%a) # // means modulo division % means remainder

# we also have boolean True and False, also None

# strings are indexed collections of characters
s = 'hello and welcome to python' # we may use ' or " '''
# all strings are immutable
s = 'changed' # this now points to a different memory location
# any indexed collection can be access using slicing
print( s[0:6:2] ) # [start:stop-before:step]
# we may iterate over any indexed collection
# we declare a code block using a colon :
for i in s: # the members are ordinal
    print(i) # by default the print statement always adds a new line character

# when the code is no longer indented, that is the end of the code block

# other collections: tuple list
# a tuple is an immutable ordinal collection of any type
t = (4, 6, 'hello', False, None, 'another string')
print(type(t), t, t[3:5])
# we can iterate
for _ in t: # we often use _ as the iterable in Python (just a convention)
    print(_)
# NB tuples are immutable (we cannot change them once created)

# a list is a mutable ordinal collection of any type
l = [6, 4, 'coffee', True, 'coffee', t, a, b, s]
# we may mutate a list as follows:
l.append('this is appended to the list')
l.insert(4, s)
l.pop() # the last member of the list is removed
l.remove('coffee') # remove the first instance of this item

print(l[0:4])
for _ in l:
    print(_, end=', ') # we may choose to override the default new-line

# -1 is often a valid number in slicing
print(s[-2::-1]) # step backwards
print(s[-3]) #changed - access the third-from-last element