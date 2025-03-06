def Outer():
    def display():
        print('hello world')
    return display

d = Outer()
d()