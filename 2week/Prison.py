a, b, c, d, e = (int(input()) for _ in range(5))
if ((b <= e and a <= d) or (a <= e and b <= d) or
        (c <= e and a <= d) or (a <= e and c <= d) or
        (b <= e and c <= d) or (c <= e and b <= d)):
    print('YES')
else:
    print('NO')
