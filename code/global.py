g = 10
def fun1():
    global g
    g = g + 5
    print('global', g)

fun1()