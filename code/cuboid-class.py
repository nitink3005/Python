class Cuboid:
    count = 0 #class variables
    def __init__(self, l, b, h):
        self.length = l #instance variable
        self.breadth = b
        self.height = h
        Cuboid.count+=1
    
    def volume(self):
        return self.length * self.breadth * self.height

    #class method
    @classmethod 
    # The @classmethod decorator tells Python that the method 
    # should receive the class itself as the first argument.
    def getCount(cls):
        return cls.count

    def setLength(self, l):
        self.length = l
    
    def getLength(self):
        return self.length


c1 = Cuboid(5, 10, 20)
c1.setLength(10)

c2 = Cuboid(5, 1, 2)
print(c1.volume())
print(c2.volume())
print(Cuboid.getCount())
print(Cuboid.count)