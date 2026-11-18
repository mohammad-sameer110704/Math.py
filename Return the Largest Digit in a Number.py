def largestDigit(n):
    if n == 0:
        return n
    n = abs(n)
    largest = 0
    while n > 0:
        x = n % 10 
        n = n // 10
        if x > largest:
            largest = x
    return largest
n = int(input("Enter a number : "))
print(largestDigit(n))
