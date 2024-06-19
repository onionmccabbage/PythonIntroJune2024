import class_a

# any class may inherit from any other class
# this lets us extend the class with new stuff

class MobileMast(class_a.Woobly):
    '''this class inherits everything from the parent class
    this class also takes a set of standards
    {'3g', '4g', '5g', '6g', '7g'}'''
    def __init__(self, t, x, st):
        super().__init__(t, x) # call the initializer of the parent
        self.standards = st # we probably need to validate
    @property
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


if __name__ == '__main__':
    mastDublin = MobileMast(12, 677, {'3g', '4g', '5g'})
    print(mastDublin.temp, mastDublin.rate, mastDublin.standards)