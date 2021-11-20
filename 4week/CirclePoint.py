def PointInCircle(x, y, xc, yc, r):
    return (((x - xc) ** 2 + (y - yc) ** 2) <= (r ** 2))

o1,o2,o3,o4,o5 = (float(input()) for _ in range(5))
if PointInCircle(o1, o2, o3, o4, o5):
    print('YES')
else:
    print('NO')
