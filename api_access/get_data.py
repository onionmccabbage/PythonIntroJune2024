# this module is all about making a call to an API over http(s)

import requests # remember - we may need to pip install requests

def getData(url):
    '''make a call to the URL and return any retrieved data
    use exception handling for robust code'''
    # check the URL is a non-empty string
    if url == '':
        raise TypeError('The URL must be a string')
    else:
        try:
            # make a call to the URL end point and retrieve a response
            response = requests.get(url) # whatev er URL was passed in to this function
            # this particular end-point always returns JSON
            data = response.json() # convert the JSON structure to Python dict or list
            if type(data)==dict:
                # we know we have ONE data structure returned
                pass # this is handy just to do nothing (while we think what to do next)
            elif type(data)==list:
                # we have a collection of data dictionaries
                pass
        except Exception as err:
            print(f'Something went wrong: {err}')


# if we have a loop we may need to break out of it
while True:
    break # stops the current loop



if __name__ == '__main__':
    api_url = 'https://jsonplaceholder.typicode.com/photos/3'
    r = getData(api_url) # we may pass an argument into our function call