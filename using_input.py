# ask the use to enter a value
# NB input is ALWAYS a string (always)
try:
    n = input('Please enter something: ')
    print(n, type(n))
    # we may cast to a different type
    n_f = float(n)
    print(n_f, type(n_f))
except Exception as err:
    print(f'Problem: {err}')
finally: # this always runs
    print('all done')