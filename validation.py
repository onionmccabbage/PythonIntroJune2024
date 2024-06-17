# we can use conditional logic to validate
n = 10 # single = will sert equality

if n>0: # > < !=  <= >= == double equals will CHECK equality
    print('we have a positive number')

# functions are objects (just like everything in Python)
def getName(): # define a function
    ask = input('Please enter a name: ')
    if ask != '':
        return f'Hello {ask}'

name = getName() # call our function
print(name)