def isPalindrome(n):
        if n == 0:
            return True
        
        rev = 0
        temp = n
        while n > 0:
            x = n % 10
            rev = rev * 10 + x
            n = n // 10
        return temp == rev