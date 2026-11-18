def countOddDigit(n):
    if n == 0 :
        return 0
    
    n = abs(n)
    c = 0
    temp = n

    while temp > 0 :
        x = temp % 10
        if x % 2 != 0:
            c  += 10
        temp = temp // 10
    return c
n = int(input("Enter a number : "))
print(countOddDigit(n))