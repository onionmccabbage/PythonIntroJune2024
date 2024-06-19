# All functions may take postional arguments and/or keyword arguments
def fnA(x, y):
    return x**y

def getPositional(*args): # by convention we use 'args'
    '''all the positonal arguments exist in a tuple'''
    print(len(args))

def getKW(**kwargs): # by convention we use 'kwargs'
    '''all the keyword arguments exist in a dict'''
    for (k,v) in kwargs.items():
        print(f'{k} is {v}')

# NB any positional arguments MUST come before any keyword arguments
def getBoth(*args, **kwargs):
    print(type(args), len(args), type(kwargs))

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
    getKW(a=True, s='wow', l=[5,4,3], t=(7.3,8.4))
    getBoth(True, [3,6,9], y=55.43, z='some data')