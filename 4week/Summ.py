def sumP():
    n = int(input())
    res = n
    if n == 0:
        return res
    if n != 0:
        res = res + sumP()
        return res


print(sumP())
