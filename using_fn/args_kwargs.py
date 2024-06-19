# All functions may take postional arguments and/or keyword arguments
def fnA(x, y):
    return x**y

def getPositional(*args): # by convention we use 'args'
    '''all the positonal arguments exist in a tuple'''
    print(len(args))

if __name__ == '__main__':
    # we may call our function using positional arguments
    r = fnA(3, 4) # 3 is at postion zero, 4 is at postition 1
    print(r)
    # or we may call founctions using keywordarguments
    r = fnA(x=3, y=4) # keyword x has value 3, keword y has a value 4
    print(r)
    getPositional() # no positional arguments
    getPositional(4) # one positional arguments
    getPositional('hello', True) # two positional arguments
    getPositional([4,3,2], (True, False), None, 'clever', fnA) # 5 positional arguments
