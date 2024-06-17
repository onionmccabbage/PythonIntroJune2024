# there is nothing special about calling this 'main'
# but we often use 'main' for the main module


# when we import, ALL the code is executed
# from util import checkNumber
import util # this imports EVERYTHING inside util

def main():
    n=3
    # check if n is an integer
    if util.checkNumber(n): # fully quality the name
        # if so, return the square of n
        return n*n
    
# exercise this code
if __name__ == '__main__':
    print(f'This module is called {__name__}') # whenever we run directly, this will be __main__

    r = main() 
    print(r) # 9