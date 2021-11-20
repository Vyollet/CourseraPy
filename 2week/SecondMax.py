n = -1
max1 = max2 = 0
while n != 0:
    if n >= max1:
        max2 = max1
    else:
        if max2 < n < max1:
            max2 = n
    if n > max1:
        max1 = n
    n = int(input())
print(max2)
