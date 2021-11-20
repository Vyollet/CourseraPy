aList = list(map(int, input().split()))
n = len(aList)
if n % 2 != 0:
    for i in range(0, n + 1, 2):
        print(aList[i], end=' ')
else:
    for i in range(0, n, 2):
        print(aList[i], end=' ')
