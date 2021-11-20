aList = list(map(int, input().split()))
n = len(aList)
k = 0
while k < n:
    if aList[k] % 2 == 0:
        print(aList[k], end=' ')
    k += 1
