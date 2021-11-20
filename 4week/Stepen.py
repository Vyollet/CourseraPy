def power(a, n):
    if n != 0:
        res = a * power(a, n - 1)
        return res
    else:
        return 1

a,n = (int(input()) for _ in range(2))
print(power(a, n))
