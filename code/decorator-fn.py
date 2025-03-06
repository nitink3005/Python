def decorator(fun):
    def wrapper():
        # do something
        print('something...')
        fun()
        print('did something...')
        # do something
    return wrapper

def display():
    print('hello')

d = decorator(display)
d()