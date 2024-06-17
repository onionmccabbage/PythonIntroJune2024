 # range is an efficient way to deal with large quantities of values

# all these values must exist in memory
t = (0,1,2,3,4,5,6,7,8,9) 
# only the range object exists in memory
r = range(0,10) # start at 0, stop-before 10

for _ in t:
    print(_, end=', ')

for _ in r:
    pass # this takes less time
    # print(_, end=', ')

# we can use a range to comprehensively carry out operations
# comprehenson
odds = [i for i in range(0,101) if i%2!=0] # we have a list
print(odds) # a list of odd number 0-100

# NB Python is I/O bound - all input and output must slow down the code execution
# every print takes time, every input takes time
# because Python asks the OS to handle I/O