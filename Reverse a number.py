def reverseNumber(n):
    if n == 0:
        return n
    if n > 0 :
        rev = 0
        temp = n
        while temp > 0:
            x = temp % 10
            rev = rev * 10 + x
            temp = temp // 10
        return rev
    else :
         rev = 0
         temp = -n
         while temp > 0 :
            x = temp % 10
            rev = rev * 10 + x
            temp = temp // 10
            return -rev

n = int(input("Enter a number : "))
print(reverseNumber(n))