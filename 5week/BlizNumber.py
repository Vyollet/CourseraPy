n = int(input())
aList = list(map(int, input().split()))
x = int(input())
r = 0
rMin = x - aList[0]
bliz = aList[0]
for i in range(1, n):
    r = x - aList[i]
    if abs(r) < abs(rMin):
        rMin = r
        bliz = aList[i]
    i += 1
print(bliz)
