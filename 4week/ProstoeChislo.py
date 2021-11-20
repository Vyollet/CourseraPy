def Prime(n):
    k = 2
    if n == 1:
        return True
    else:
        while k ** 2 <= n and n % k != 0:
            k += 1
        return k ** 2 > n

n = int(input())
if Prime(n):
    print("YES")
else:
    print('NO')
