import math

def Min(n):
    i = 0
    min = 1
    sq = math.sqrt(n)
    while i <= sq:
        if i != 0 and n % i == 0 and n // i < n:
            min = i
            break
        else:
            min = n
        i += 1
    return min

print(Min(int(input())))
