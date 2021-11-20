x,y = (int(input()) for _ in range (2))
if (y % (y - x + 1)) == 0:
    print('YES')
else:
    print('NO')
