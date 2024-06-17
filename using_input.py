# ask the use to enter a value
# NB input is ALWAYS a string (always)
try:
    n = input('Please enter something: ')
    print(n, type(n))
    # we may cast to a different type
    n_f = float(n)
    print(n_f, type(n_f))
# we typically handle specific exceptions first
except ValueError as ve:
    print(f'That cannot be cast as a float {ve}')
# ... then generic exceptions later
except Exception as err:
    print(f'Problem: {err}')
finally: # this always runs
    print('all done')