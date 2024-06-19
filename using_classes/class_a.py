# the most simple class in Python

# in Python everything is an object
# so every class, every list, tuple, dict, modules, packages, set are all objects
class Woobly:
    '''here we capture temperature and data-throughput as properties'''
    def __init__(self, t, x): # every function inside a class MUST take 'self'
        '''This function will be called every time we create an instance of this class'''
        self.temp = t
        self.rate = x



if __name__ == '__main__':
    # we may choose to create instances of any class
    w1 = Woobly(12, 866)
    w2 = Woobly(6, 1024)
    w3 = Woobly(28, 64)
    l1 = list() # we now have an instance of the list class
    d1 = dict()
    s1 = set()
    a1 = str()
    print(w1, type(w1), w1.temp, w1.rate) # we use dot otation to acess properties of a class instance