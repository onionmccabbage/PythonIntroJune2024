def isLessThan100(n):
    '''is the value n les than 100'''
    return 'less than 100' if n<100 else 'not less than 100'

if __name__ == '__main__':
    print( isLessThan100(99) )
    print( isLessThan100(199) )
    print( isLessThan100(100) )