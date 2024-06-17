# everything that is not indented is considered to be the global scope
g = 'this is in the global scope'

# anything within a code block has its own scope
def fnA():
    global g # we now have access to the value in the global scope
    g = 'this is in a local scope'
    return g

if __name__ == '__main__':
    print(g)
    print( fnA() )
    print(g)