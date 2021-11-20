aList = list(map(int, input().split()))
o = int(aList[0])
summ,k = 0
bList = [None] * aList[1]
for i in range(0, len(bList)):
    bList[i] = int(input())
cList = sorted(bList)
for j in range(0, len(cList)):
    summ = summ + cList[j]
    if summ > o:
        break
    elif summ == 0:
        k += 1
    else:
        j += 1
        k += 1
print(k)
