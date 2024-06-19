# functional programing with map and filter

def isOdd(n): # n should be an integer
    '''return True if the n is odd, Fasle otherwise'''
    return n%2 != 0

if __name__ == '__main__':
    print( isOdd(3) ) # True (it is odd)
    print( isOdd(8) ) # False (not odd)