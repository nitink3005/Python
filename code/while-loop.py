count = 0
while count < 10:
    n = int(input("Enter a number"))
    if n%3 == 0:
        continue
    print(count, "hello world")
    count = count + 1
    if count > 10:
        break