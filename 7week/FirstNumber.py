chisla = list(map(int, input().split()))
povSet = set()
for i in chisla:
    if i in povSet:
        print('YES')
    else:
        print('NO')
    povSet.add(i)
