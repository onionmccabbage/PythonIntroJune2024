# every file on a computer is a byte file
# some are also human readable as text files

def writeBytes(b):
    '''commit some bytes to a file'''
    with open('byte_file', 'ab') as bout: # 'ab' will append bytes
        bout.write(b)

def readBytes():
    '''retrieve content fro ma byte file'''
    with open('byte_file', 'rb') as bin: # 'rb' will read bytes
        r = bin.read()
    return r

if __name__ == '__main__':
    '''we need some bytes'''
    my_bytes = b'this will be encoded as a byte string'
    other_bytes = 'this is text'.encode()
    writeBytes(my_bytes)
    b = readBytes()
    b_text = b.decode() # convert bytes back to text
    print(b, type(b))
