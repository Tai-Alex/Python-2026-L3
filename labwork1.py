choose = int(input("Choose your exercise: "))

if choose == 1:
    r = float(input("Enter circle radius? "))
    print("Circle area =", round(r * r * 3.14, 1))

if choose == 2:
    t = float(input("Enter the temperature in Celsius? "))
    print(t, "(C) =", t * 1.8 + 32, "(F)")

if choose == 3:
    n = int(input("Enter a number? "))
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        print(n, "is a prime number")
    else:
        print(n, "is a NOT prime number")

if choose == 4:
    n = int(input("Enter a number? "))
    sum = 0
    for i in range(1, int(n / 2) + 1): 
        if n % i == 0: sum += i
    if sum == n: print(n, "is a perfect number")
    else: print(n, "is a NOT perfect number")

if choose == 5:
    lst = ["Red", "Green", "Blue", "Yellow", "Pink", "White", "Black", "Brown", "Orange", "Silver"]
    color = str(input("What is your favorite color? "))
    if color in lst: print("Your color is at index", lst.index(color), "in my list")
    else: print("Sorry, I could not find your color")
    
if choose == 6:
    print("range1:", end = " ")
    for i in range(7): print(i, end = " ")
    print("\nrange2:", end = " ")
    for i in range(1, 11, 3): print(i, end = " ")
    print("\nrange3:", end = " ")
    for i in range(5, 0, -1): print(i, end = " ")
    print("\nrange4:", end = " ")
    for i in range(6, -3, -2): print(i, end = " ")

if choose == 7:
    def remove_dollar_sign(s):
        s = s.replace("$", "")
        return s
    s = str(input("Type your string: "))
    new_s = remove_dollar_sign(s)
    print(new_s)

if choose == 8:
    lst = [1, 4, 5, -1, 10]
    def even(lst):
        new_lst = []
        for i in lst:
            if i % 2 == 0: new_lst.append(i)
        return new_lst
    print(even(lst))

if choose == 9:
    def factorial(n):
        S = 1
        for i in range(1, n + 1): S *= i
        return S
    n = int(input("Enter your number: "))
    print(factorial(n))

if choose == 10:
    def div(n):
        for i in range(1, n + 1):
            if n % i == 0: print(i, end = " ")
    n = int(input("Enter a number: "))
    div(n)

if choose == 11:
    import math
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    a = x2 - x1; b = y2 - y1
    d = math.sqrt(a ** 2 + b ** 2)
    print("Distance between 2 points: ", round(d, 2))

if choose == 12:
    m, n = map(int, input().split())
    for i in range(n): print("*", end = " ")
    print("")
    for i in range(m - 2): 
        for j in range(n):
            if (j == 0 or j == n - 1): print("*", end = " ")
            else: print(end = "  ")
        print("")
    for i in range(n): print("*", end = " ")





















    