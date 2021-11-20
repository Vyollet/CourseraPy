def bPower(a, n):
    if n != 0:
        if n % 2 == 0:
            return bPower(a ** 2, n/2)
        if n % 2 != 0:
            return a * bPower(a, n - 1)
    else:
        return 1


one, two = (float(input()) for _ in range (2))
print(bPower(one, two))
