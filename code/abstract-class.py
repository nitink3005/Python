from abc import ABC, abstractmethod
class Parent(ABC):
    @abstractmethod
    def show(self):
        pass
    
    def display(self):
        print('parent display')

class Child(Parent):
    def show(self):
        print('child class')

class Child2(Child):
    def show(self):
        pass

c = Child()
c.show()
c.display()

d = Child2()
print(Child2.mro())