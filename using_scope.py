# everything that is not indented is considered to be the global scope
g = 'this is in the global scope'

# NB in Python scope and namespace can mean the same thing

# anything within a code block has its own scope
def fnA():
    global g # we now have access to the value in the global scope
    g = 'which scope is this?' # depends if we say 'global'
    return g

if __name__ == '__main__':
    print(g)
    print( fnA() )
    print(g)