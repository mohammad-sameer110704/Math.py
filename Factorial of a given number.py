def factorial(n):
    if n == 0 :
        return 1
    if n < 0 :
        return "Number is less than 0 , Please enter a valid number"
    fact = 1
    for i in range (n) :
        fact = fact * (n - i)
    return fact
n = int(input("Enter a number gratter than ZERO : "))
print(factorial(n))