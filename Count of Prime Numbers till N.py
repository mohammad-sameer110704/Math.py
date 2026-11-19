def primeUptoN(n):
    c = 0
    for i in range(n + 1):
        p = 0

        for j in range(1, i + 1):
            if i % j == 0:
                p += 1

        if p == 2:
            c += 1

    return c
n = int(input("Enter a number gratter than ZERO : "))
print(primeUptoN(n))