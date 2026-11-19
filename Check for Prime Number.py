def isPrime(n):
    if n <= 1 :
        return False,"It's not a Prime"
    p = 0
    for i in range (2,n+1):
        if n % i == 0:
            p += 1
    return p == 1,"It's a Prime"
n = int(input("Enter a number greater than 0 : "))
print(isPrime(n))