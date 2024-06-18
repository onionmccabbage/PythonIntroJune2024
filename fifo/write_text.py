# rules for identifiers
# we may use letters,numbers and underscore for any identifier
# fist character NOT a digit
# identifier: module name, a variable name, a function name a class name...
# a package is a folder in which we gather related python modules

def printTofile(s):
    '''send printed output to a text file'''
    # we need a file access object
    fout = open('my_file.txt', 'at') # 'at' will append text
    # by default print sends its output to the terminal console
    print(s, file=fout) # redirect the print output to our file access object

def writeToFile(s):
    '''write text to a file'''
    fout = open('my_file.txt', 'at')
    fout.write(s) # send our stringo f text to the file access object 'write' stream

if __name__ == '__main__':
    # here we exercise the local code
    words = 'Here is some text we need to persist in a file'
    printTofile(words)
    writeToFile(words)