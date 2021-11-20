aList = list(map(int, input().split()))
n = len(aList)
k = 0
kolvo = 0
while k < n:
    if aList[k] > 0:
        kolvo += 1
    k += 1
print(kolvo)
