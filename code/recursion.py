def factorial(n):
    if n == 0:
        return 1
    else:
        res = n * factorial(n-1)
        return res

res = factorial(5)
print(res)