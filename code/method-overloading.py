class Arith:
    def sum(self, a, b, c = None):
        sum = a + b
        if c == None:
            return sum
        else:
            return sum + sum

a = Arith()
print(a.sum(5, 10))
print(a.sum(5, 10, 20))