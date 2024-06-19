import class_a

# any class may inherit from any other class
# this lets us extend the class with new stuff

class MobileMast(class_a.Woobly):
    '''this class inherits everything from the parent class
    this class also takes a set of standards
    {'3g', '4g', '5g', '6g', '7g'}'''
    def __init__(self, t, x, st):
        super().__init__(t, x) # call the initializer of the parent
        self.standards = st

if __name__ == '__main__':
    mastDublin = MobileMast(12, -677)
    print(mastDublin.temp, mastDublin.rate)