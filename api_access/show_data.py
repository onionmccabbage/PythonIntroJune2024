# this module is responsible for revealing any retrieved data

def showData(d):
    '''reveal the data by printing it'''
    message = ''
    if type(d)==dict:
        '''iterate over the key-value pairs and show them nicely'''
        for (k,v) in d.items():
            message += f'{k} is {v}\n'
    if type(d)==list:
        '''iterate over the list then show each dict nicely'''
        for _ in d:
            message += f'{_}\n'
    return message

if __name__ == '__main__':
    d = 'does this work?'
    showData(d)