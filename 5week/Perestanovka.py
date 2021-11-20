aList = list(map(int, input().split()))
n = len(aList)
bList = []
i = 0
while i < n - 1:
    bList.append(aList[i + 1])
    bList.append(aList[i])
    i += 2
if n % 2 != 0:
    bList.append(aList[-1])
print(*bList)
