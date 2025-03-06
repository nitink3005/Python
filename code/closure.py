def hello():
    msg = 'hello world'
    def display():
        print('*' * 10)
        print(msg)
        print('*' * 10)
    return display

d = hello()
d()
