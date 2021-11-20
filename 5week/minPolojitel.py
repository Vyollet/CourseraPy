aList = list(map(int, input().split()))
k = 0
while aList[k] <= 0:
    k += 1
min = aList[k]
while 0 <= k <= len(aList) - 1:
    if aList[k] < min and aList[k] > 0:
        min = aList[k]
    k += 1
print(min)
