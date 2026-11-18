def reverseNumber(n):
    if n == 0:
        return n
    if n > 0 :
        rev = 0
        while n > 0:
            x = n % 10
            rev = rev * 10 + x
            n = n // 10
        return rev
    else :
         rev = 0
         n = -n
         while n > 0 :
            x = n % 10
            rev = rev * 10 + x
            n = n // 100
         return -rev

n = int(input("Enter a number : "))
print(reverseNumber(n))