# in this main module we will import useful stuff from other modules
from get_data import getData

def main(root, category, id):
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
    r = main('https://jsonplaceholder.typicode.com', 'todos', 4)
    print(r, type(r))