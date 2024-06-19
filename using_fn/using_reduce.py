from functools import reduce # this is always available in the Python standard library
from random import randint

def addThem(a,b):
    '''return the sum of a and b'''
    return a+b

if __name__ == '__main__':
    r = range(1,11)
    # we may need to cumulatively add all these values
    total = reduce(addThem, r)
    print(total) # 55
    # we may need to populate a colleciton
    rand = []
    for _ in range(0, 10*4):
        rand.append( randint(0,10) )
    # what is the average?
    tot = reduce(addThem, rand)
    num_values = len(rand)
    aver = tot/num_values
    print(aver) # about 5:0
    # limits of Python - mostly to do with the limits of computers!
    print(10**1000)