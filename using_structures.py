drinks_t = ('coffee', 'tea', 'water', 'juice')
# dictionary and set are structures with no ordinal sequence
# (they are not numerically indexed)
# a dict is a collection of key:value pairs of any data type
d = {'name':'Ottily', 'age':82, 'auth':False}
# we may specify new dict members
d['break'] = drinks_t[0] # we have no control where in the dict this will be
print(d, type(d), d['age']) # we cannot access the list 'l' it is not in this module
# we can iterate over a dictionary
for (k,v) in d.items():
    print(k, v)