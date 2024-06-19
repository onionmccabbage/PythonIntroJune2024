# functional programing with map and filter

def isOdd(n): # n should be an integer
    '''return True if the n is odd, False otherwise'''
    return n%2 != 0

# challenge: how can we determine if a number is a square number
def isSquare(n): 
    ''' return the number if it is a square, otherwise return nothing'''
    if n**0.5 == int(n**0.5):
        return n**0.5 == int(n**0.5)

if __name__ == '__main__':
    print( isOdd(3) ) # True (it is odd)
    print( isOdd(8) ) # False (not odd)
    # we may use our isOdd function to map across a bunch of values
    values = range(-9,10) # all the integers from -9 to 9
    odds = map(isOdd, values) # each value will be injected into our function
    print(odds) # we have a map object
    for _ in odds:
        print(_)
    # work with our sqrt fn
    print( isSquare(3) )
    c = range(1, 101)
    sq = map(isSquare, c)
    for _ in sq:
        print(_)
    # we may also use filter....
    just_the_odds = filter(isOdd, values)
    for _ in just_the_odds:
        print(_)
    just_the_squares = filter(isSquare, c)
    for _ in just_the_squares:
        print(_)
