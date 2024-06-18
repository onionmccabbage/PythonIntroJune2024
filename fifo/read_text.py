def readFromTextFile():
    '''retrieve text from a file'''
    # NB it would be good to use try-except for ANY file access
    # 'rt' will read text
    fin = open('my_file.txt', 'rt')
    # t = fin.read() # read back the entire file
    # t = fin.readline(10) # read back the line, or n characters of the first line
    # t = fin.readlines() # retrieve a list with each line as a member
    # can we access specific content...
    t = ''
    for _ in range(0, 1025, 32):
        fin.seek(_, 0) # whence may be 0 (start of file) 1 (current position) or 2 (end of file)
        t += fin.readline() # ....
    fin.close()
    return t

def elegant():
    '''we can use 'with' as an elegant technique'''
    with open('my_file.txt', 'rt') as fin:
        r = fin.read()
        # when we use 'with' the resource will be closed when done
    return r

# NB in all file access cases it is a good idea to use try-except

if __name__ == '__main__':
    txt = readFromTextFile()
    print(txt) # see what we have
    # print(type(txt))
    # for _ in txt:
    #     print(_)
    # retrieved = elegant()
    # print(retrieved)