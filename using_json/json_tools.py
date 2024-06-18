import json # the tools to work with JSON are available for import

def useJSON():
    '''here we explore techniques to work with JSON data'''
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )
    # we can convert ANY structure to JSON
    creatures_j = json.dumps(creatures_t) # convert to text (JSON)
    print(creatures_j, type(creatures_j))
    # we can convert JSON text back to a Python structure
    creatures_l = json.loads(creatures_j)
    print(creatures_l, type(creatures_l))
    # we can work with individual parts
    alb = creatures_l[0]
    print(alb, type(alb))
    # we can convert this dict to JSON text
    alb_j = json.dumps(alb)
    print(alb_j, type(alb_j))
    # ...and back again to a dict
    alb_d = json.loads(alb_j) # convert JSON text into a python stucture
    print(alb_d, type(alb_d))

    # we may write to a JSON text file
    with open('albatros.json', 'at') as fout:
        json.dump(alb_j, fout) # this will commit the JSON text to a file
    # we may read JSON back again...(as JSON text)
    with open('albatros.json', 'rt') as  fin:
        json.load(fin)
    




if __name__ == '__main__':
    useJSON()