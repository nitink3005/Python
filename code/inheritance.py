class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    
    def area(self):
        return self.length * self.breadth

#example of inheritance
class cuboid(Rectangle):
    def __init__(self, l, b,h):
        self.height = h
        super().__init__(l, b)
    
    def volume(self):
        return self.length * self.breadth * self.height

c1 = cuboid(5, 20, 10)
print(c1.volume())
print(c1.area())