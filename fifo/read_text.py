def readFromTextFile():
    '''retrieve text from a file'''
    # NB it would be good to use try-except for ANY file access
    # 'rt' will read text
    fin = open('my_file.txt', 'rt')
    # t = fin.read() # read back the entire file
    t = fin.readline(10) # read back the line, or n characters of the first line
    fin.close()
    return t

if __name__ == '__main__':
    txt = readFromTextFile()
    print(txt) # see what we have