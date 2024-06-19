# there are many features built in the Python objects
# we can override practically all of them
# here we will override what it means to be equal
class Word(object): # NB we may choose ot explicitly inherit from object
    '''Here we encapsulate a string, whre equality is case-insensitive'''
    def __init__(self, w):
        self.w = w # we might choose to write get/set here...
    def __eq__(self, otherWord):
        '''we override the built in __eq__ (for equality)'''
        return self.w.lower() == otherWord.w.lower()

# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object


if __name__ == '__main__':
    w1 = Word('hello')
    w2 = Word('Hello')
    print(w1 == w2) # True (case-insensitive comparison)
    # print(w1.lower()==w2.lower()) # True