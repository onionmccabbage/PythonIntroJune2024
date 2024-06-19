class A:
    __slots__ = ['__x']
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, new_x):
        if type(new_x) in (int, float):
            self.__x = new_x
        else:
            raise TypeError
        
if __name__ == '__main__':
    a = A(8)
    # a.c = False
    a.__c = False
