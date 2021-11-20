n = int(input())
varianti = set(range(1, n + 1))
vBeatris = input()
while vBeatris != 'HELP':
    vBeatris = set(map(int, vBeatris.split()))
    otvAvgust = input()
    if otvAvgust == 'YES':
        varianti &= vBeatris
    else:
        varianti -= vBeatris
    vBeatris = input()
print(*sorted(varianti))
