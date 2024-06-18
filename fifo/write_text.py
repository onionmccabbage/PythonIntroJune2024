# rules for identifiers
# we may use letters,numbers and underscore for any identifier
# fist character NOT a digit
# identifier: module name, a variable name, a function name a class name...
# a package is a folder in which we gather related python modules

def printTofile(s):
    '''send printed output to a text file'''

def writeToFile(s):
    '''write text to a file'''

if __name__ == '__main__':
    # here we exercise the local code
    words = 'Here is some text we need to persist in a file'
    printTofile(words)
    writeToFile(words)