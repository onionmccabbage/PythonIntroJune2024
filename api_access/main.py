# in this main module we will import useful stuff from other modules
import sys
from get_data import getData
from show_data import showData

def main(root, category, id=0): # we may choose to pass a default for any argument
    '''operate our code'''
    if root == '':
        raise TypeError('root URL must be a string')
    if category in ('todos', 'photos', 'posts'):
        url = f'{root}/{category}' # join the root URL with the category
    else:
        raise TypeError('Category can only be todos, photos or posts')
    if id > 0:
        url +=f'/{id}' # we only append ID if it is a positive number
    # so at this point we will have a URL that may include an ID
    # we can call our getData function which we imported earlier
    result = getData(url)
    return result

if __name__ == '__main__':
    # check to see if we have any additonal system argument variables
    if len(sys.argv)>1: # do we have additional sys.argv members?
        cat = sys.argv[1]
        id  = int(sys.argv[2]) # careful - every sys.argv will be a string
        r = main('https://jsonplaceholder.typicode.com', cat, id)
        print( showData(r) )
    r = main('https://jsonplaceholder.typicode.com', 'photos', 8)
    print( showData(r) )
    # print(r, type(r))
    r = main('https://jsonplaceholder.typicode.com', 'todos') # id will defautl to zero
    print( showData(r) )
    # print(r, type(r))
    r = main('https://jsonplaceholder.typicode.com', 'posts', 1)
    print( showData(r) )
    # print(r, type(r))
    # we can check the exceptions...
    r = main('', 'posts', 1) # this stops dead because of the exception
    r = main('https://wibblywooblywub.com', 'posts', 1)