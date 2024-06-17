# if we managed to pip install the requests library, we can...
import requests

# the requests library lets us access external APIs via http
def getOnePhoto():
    '''make a requetss to an API to retrieve data for one photo'''
    apiUrl = 'https://jsonplaceholder.typicode.com/photos/3'
    #if we need to authenticate, we use 'post' and send 'headers'
    response = requests.get(apiUrl) # make a request
    # The requests library understands JSON, XML, text etc.
    data = response.json() # we now have the data
    return data

if __name__ == '__main__':
    result = getOnePhoto()
    print(result)