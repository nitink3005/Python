def add(a, b, /, c, d, e, f):
    print(a, b, c, d, e, f)
    return a + b + c + d + e + f

add(2, 5, 3, f = 100, e = 20, d = 1)


def add2(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
    return a + b + c + d + e + f

add2(2, 5, e = 10, f = 100, c = 20, d = 1)