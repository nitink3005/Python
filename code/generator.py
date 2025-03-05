def Days():
    L = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    i = 0
    while True:
        x = L[i]
        i = (i+1)%7
        yield x

d = Days()
print(next(d))
print(next(d))
print(next(d))
print(next(d))