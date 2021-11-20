a, b, c, d = int(input()),  int(input()),  int(input()), int(input())
if a != 0 and c != 0 and b % a == 0:
    x = b // a
    x2 = d // c
    if x != x2:
        print(-x)
    else:
        print('NO')
elif a != 0 and c == 0:
    print(- b // a)
elif a == 0 and c != 0:
    print('INF')
elif a == 0 and c == 0:
    print('NO')
else:
    print('NO')
