k = kMax = kMin = 0
aList = list(map(int, input().split()))
max,min = (int(aList[k]) for _ in range (2))
while 0 <= k <= len(aList) - 1:
    el = int(aList[k])
    if el >= max:
        max = aList[k]
        kMax = k
    elif el < min:
        min = aList[k]
        kMin = k
    k += 1
aList[kMax] = min
aList[kMin] = max
print(*aList)
