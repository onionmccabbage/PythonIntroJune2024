import class_a

# any class may inherit from any other class
# this lets us extend the class with new stuff

class MobileMast(class_a.Woobly):
    '''this class inherits everything from the parent class
    this class also takes a set of standards
    {'3g', '4g', '5g', '6g', '7g'}
    Methods of this class:
    checkTemp will return True if ok, False if out of bounds -12 to +38
    activateHeatAC will activate heaters or air con'''
    __slots__ = ['__temp', '__rate', '__standards'] # a list of permitted mangled properties
    def __init__(self, t, x, st):
        super().__init__(t, x) # call the initializer of the parent
        self.standards = st # we probably need to validate
    @property # NB these functions appear as properties of this class
    def standards(self):
        return self.__standards
    @standards.setter
    def standards(self, new_st_set):
        '''we only permit a set and that set may only contain {'3g', '4g', '5g', '6g', '7g'}'''
        if type(new_st_set)==set:
            permitted = {'3g', '4g', '5g', '6g', '7g'}
            for item in new_st_set:
                if item not in permitted:
                    raise TypeError('Not a permitted standard')
            self.__standards = new_st_set # all good
        else:
            raise TypeError('Standards must be a set of permitted values')
    def checkTemp(self):
        '''return True or False based on sytem temperature'''
        if self.temp <-12 or self.temp > 38:
            return False
        else:
            return True
    def activateHeatAC(self):
        if self.temp < -12: # use the temp getter to check the value
            self.heater = True # direct access (not manged, not get/set methods)
        elif self.temp > 38:
            self.ac = True # this property (self.ac) is DIRECTLY AVAIABLE
        else:
            self.ac = False
            self.heater = False
    def __str__(self): # we may override the built in __str__ method
        '''__str__ is used by the print method'''
        output = f'Temperature is {self.temp} data rate is {self.rate} supported standards: {self.standards}'
        return output
    def __repr__(self):
        '''__repr__ is used to represent in immediate mode python'''
        return self.__str__() # use same as print!!!

if __name__ == '__main__':
    mastDublin = MobileMast(12, 677, {'3g', '4g', '5g'})
    # by default this class instance is just like any other object
    # that means we can assign any arbitrary property to it
    mastDublin.__isitcoffeeyet = True
    # print(mastDublin.temp, mastDublin.rate, mastDublin.standards)
    print(mastDublin) # this will use our __str__ method
    # we can use the mehtods of this class
    print(mastDublin.checkTemp()) # True or False
    # chage teh temp out of bounds, then call our gheater/ac method to torun on the equipment
    mastDublin.temp = -24 # too cold
    mastDublin.activateHeatAC() # this should turn on the heater
    print(f'Heater on: {mastDublin.heater}') # True

    print(f'does this exist: {mastDublin.__isitcoffeeyet}')