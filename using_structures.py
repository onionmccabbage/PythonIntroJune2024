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
    # print formatting
    # print(k, v)
    # f'   {}   ' lets us inject any value or statement into a print string
    print( f'{k} is {d[k]} ' ) # f means format the print

# a set is a collection of un-indexed unique values of any type
my_set = {4, 0, 1, 7, 2, 9, True, 'anything', 4, 2, True} # curly brackets mean both a dict and a set. Context determins which
my_set.add(False)
my_set.add(4) # the unique member exists once
my_set.add(None)
my_set.add(5.431)
# NB be careful 1 and True evaluate to the same thing!!!
# (0 and False evaluate the same)
print(my_set, type(my_set))