# here are some useful utilities we may need to reuse

def checkNumber(n):
    '''return True if n is a number, Fasle otherwise'''
    if type(n)==int:
        return True
    else:
        return False
    
# exercise the code
if __name__ == '__main__':
    # python always assigns a name to a running module
    print(f'This module is called {__name__}') # whenever we run directly, this will be __main__
    # but if a module is imported, it will have the module name
    print( checkNumber(3) )   # True
    print( checkNumber('3') ) # False

