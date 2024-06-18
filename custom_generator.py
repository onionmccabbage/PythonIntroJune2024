import datetime
# the range object is dead handy for generating a range of values
# NB range can only handle integer values
r = range(1, 1001, 50) # all the numbers from -1000 to 1000 every 50

for _ in r:
    print(_)

# comprehension - we comprehensively deal with every member in a collection
fiftieths = [1/i for i in r] # we have a list (in memory)
print(fiftieths)

# comprehension may create a generator
# generators do not occupy much memory, but they can yield sucessive values
roots = (i**0.5 for i in r) # this is NOT a list it is a generator

print(type(roots))
# we may iterate over a generator
for _ in roots:
    print(_) # each value is yielded at the moment we need it

def getDate():
    '''return a nicely formatted string with todays date'''
    now = datetime.datetime.now() # we have a date-time object representing the mpment it was called
    ds = now.strftime('%d-%m-%Y %H:%M:%S') # a date-time picture
    return ds

print( getDate() )  

# we may create our own generator
def getTimeStamp():
    '''this generator will yield the time at the moment it is needed'''
    while True: # this generator will only stop when our module ends
        now = datetime.datetime.now()
        ts = now.strftime('%H:%M:%S') # we may format any way we like
        yield ts # instead of 'return' we say 'yield'

if __name__ == '__main__':
    ts_gen = getTimeStamp() # we now have an instance of our generator
    print( ts_gen.__next__() )  # this will grab the next value from our generator
    # we may choose to iterate over a generator
    for _ in range(0,10**3):
        print(ts_gen.__next__())