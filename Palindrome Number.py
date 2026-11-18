def isPalindrome(n):
        if n == 0:
            return True
        n = abs(n)
        if n > 0 :
            rev = 0
            temp = n
            while n > 0:
                x = n % 10
                rev = rev * 10 + x
                n = n // 10
            return temp == rev
        else :
            rev = 0
            temp = n
            while n > 0:
                x = n % 10
                rev = rev * 10 + x
                n = n // 100
            return temp == rev
n = int(input("Enter a number : "))
print(isPalindrome(n))