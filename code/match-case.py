day = int(input("Enter day number: "))
match day :
    case 1:
        print("Sunday")
    case 2: 
        print("monday")
    case _:
        print("holiday")