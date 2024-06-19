# the most simple class in Python

# in Python everything is an object
# so every class, every list, tuple, dict, modules, packages, set are all objects
class Woobly:
    '''here we capture temperature and data-throughput as properties'''
    def __init__(self, t, x): # every function inside a class MUST take 'self'
        '''This function will be called every time we create an instance of this class'''
        self.temp = t # this will call our temp setter function
        self.rate = x
    # we use property decorators to declare set/get methods for our properties
    @property
    def temp(self):
        return self.__temp # mangling __ (not directly aaccessible)
    @temp.setter
    def temp(self, new_temp):
        '''validate that hte temperature is within bounds'''
        if type(new_temp) in (int, float):
            self.__temp = new_temp
        else:
            raise TypeError
    @property
    def rate(self):
        return self.__rate
    

if __name__ == '__main__':
    # we may choose to create instances of any class
    w1 = Woobly(12, 866) # here the arguments are simple values
    w2 = Woobly(6, 1024) # it is entirely possible to pass structures  (tuple, list, dic...) as arguments
    w3 = Woobly(28, 64)
    l1 = list(23, 488) # we now have an instance of the list class
    d1 = dict({'temp':23, 'rate':488})
    d1['temp'] = True # this is not a valid temperature
    s1 = set()
    a1 = str('23degrees 488baud') # temp and rate
    print(w1, type(w1), w1.temp, w1.rate) # we use dot otation to acess properties of a class instance
    print(f'The instance w2 has temperature of {w2.temp} and rate {w2.rate}')