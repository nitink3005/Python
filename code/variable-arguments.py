def fun1(*args):
    print(type(args), args)

fun1()
fun1(10, 20)
fun1(30, 20, 10)

# <class 'tuple'> ()
# <class 'tuple'> (10, 20)
# <class 'tuple'> (30, 20, 10)