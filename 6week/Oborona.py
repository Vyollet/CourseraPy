n = int(input())
iN = list(map(int, input().split()))
m = int(input())
iM = list(map(int, input().split()))
posel = []
bomb = []
for i in range(n):
    posel.append([i, iN[i], 0])
for i in range(m):
    bomb.append([i, iM[i]])
posel.sort(key=lambda q: q[1])
bomb.sort(key=lambda q: q[1])
j = 0
for i in range(0, n):
    rast = abs(posel[i][1] - bomb[j][1])
    while j < len(bomb)-1 and \
            rast > abs(posel[i][1] - bomb[j+1][1]):
        j += 1
        rast = abs(posel[i][1] - bomb[j][1])
    else:
        posel[i][2] = bomb[j][0] + 1
posel.sort(key=lambda q: q[0])
i = 0
for i in range(0, n):
    print(posel[i][2], end=' ')
