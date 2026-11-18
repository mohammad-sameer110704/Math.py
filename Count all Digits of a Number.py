def countDigit(n):
    if n == 0:
        return 1
    n = abs(n)
    c = 0
    while n > 0 :
        n = n // 10
        c +=10
    return c
n = int(input("Enter a Number : "))
print(countDigit(n))