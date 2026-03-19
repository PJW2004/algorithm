for _ in range(int(input())):
    name,grade=input().split()
    grade = int(grade)
    if grade > 96:
        print(name + " A+")
    elif grade > 89:
        print(name + " A")
    elif grade > 86:
        print(name + " B+")
    elif grade > 79:
        print(name + " B")
    elif grade > 76:
        print(name + " C+")
    elif grade > 69:
        print(name + " C")
    elif grade > 66:
        print(name + " D+")
    elif grade > 59: 
        print(name + " D")
    else:
        print(name + " F")