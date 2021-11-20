aList = list(map(int, input().split()))
n = len(aList)
k = 1
while k < n:
    if aList[k] > aList[k-1]:
        print(aList[k], end=' ')
    k += 1
