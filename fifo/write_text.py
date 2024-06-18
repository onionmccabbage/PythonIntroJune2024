# rules for identifiers
# we may use letters,numbers and underscore for any identifier
# fist character NOT a digit
# identifier: module name, a variable name, a function name a class name...
# a package is a folder in which we gather related python modules

def printTofile(s):
    '''send printed output to a text file'''
    # we need a file access object
    try: # whenever we deal with files, there might be a problem
        # 'at' will append text, 'xt' will exclusively write text. 'wt' will (over)write
        # we may use an absolute or relative path to the file
        fout = open('my_file.txt', 'at') # xt fails if file exists
        # by default print sends its output to the terminal console
        print(s, file=fout) # redirect the print output to our file access object
        fout.close()
    except Exception as err:
        print(f'There was a problem: {err}')

def writeToFile(s):
    '''write text to a file'''
    fout = open('my_file.txt', 'at')
    # fout.write(s) # send our string of text to the file access object 'write' stream
    fout.write(f'{s}\n') # we MAY choose to add a new line
    fout.close() # always a good idea to tidy up

if __name__ == '__main__':
    # here we exercise the local code
    words = 'Here is some text we need to persist in a file'
    # printTofile(words) # uses print (ends with a new line )
    for _ in range(0, 10):
        writeToFile(f'{str(_)*32}') # does not use print ( no default new line at the end)