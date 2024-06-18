def readFromTextFile():
    '''retrieve text from a file'''
    # NB it would be good to use try-except for ANY file access
    # 'rt' will read text
    fin = open('my_file.txt', 'rt')
    # t = fin.read() # read back the entire file
    # t = fin.readline(10) # read back the line, or n characters of the first line
    t = fin.readlines() # retrieve a list with each line as a member
    # can we access specific content...
    # fin.seek(8, 1) # whence may be 0 (start of file) 1 (end of file) or 2
    # t = fin.readline() # ....
    fin.close()
    return t

if __name__ == '__main__':
    txt = readFromTextFile()
    print(txt) # see what we have
    # print(type(txt))
    # for _ in txt:
    #     print(_)