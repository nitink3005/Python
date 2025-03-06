def Outer():
    def Inner():
        print('I am inner function')

    Inner()

Outer()