import random # this is part of the Python standard library

# it is good practice to docunment your code
def getRandInt():
    '''return a random integer between 1 and 10
    this function takes no arguments'''
    return random.randint(1,10)

# we may choose to pass arguments into our function
def guessNumber(r):
    '''iterate until we hit the random number'''
    for _ in range(1,11): # a range returns each value from (start, stop-before)
        if _ == r:
            return f'The number is {_}'

def userGuess():
    r = getRandInt() # we have another random number
    # we could use a runloop
    while True: # this loop will carry on endlessly
        ask = input('guess:')
        ask_n = float(ask) # remember - input is ALWAYS a string
        if ask_n == r:
            print(f'You guessed {r}')
            break #  this stops the loop

# immediate code is run procedurally
# r = getRandInt() # we now have a random integer
# result = guessNumber(r) # pass in r as an argument
# print( result )

userGuess() # call the function!!!


