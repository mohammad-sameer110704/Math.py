def isArmstrong(n):
    if n == 0:
        return 0
    n = abs(n)
    temp = n
    p = 0
    while temp > 0 :
        temp  = temp // 10
        p += 1
    s = 0
    temp = n
    while temp > 0 :
        x = temp % 10
        s += x ** p
        temp = temp // 10
    return s == n
n = int(input("Enter a number : "))
print(isArmstrong(n))