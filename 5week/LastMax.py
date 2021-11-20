aList = list(map(int, input().split()))
k = 0
max = int(aList[k])
kMax = 0
while 0 <= k <= len(aList) - 1:
    el = int(aList[k])
    if el >= max:
        max = aList[k]
        kMax = k
    k += 1
print(aList[kMax], kMax)
