def divisors(n):
    if n < 0 :
        return "Invalid number, Number is less than 0 "
    if n == 1 :
        return [1]
    output = []
    for i in range (1,n+1) :
        if n % i == 0 :
            output.append(i)
    return output
n = int(input("Enter a number greatter than 0 : "))
print(divisors(n))