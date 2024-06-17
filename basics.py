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