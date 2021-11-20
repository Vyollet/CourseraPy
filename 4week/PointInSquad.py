def IsPointInSquare(x, y):
    result = (-1 <= x <= 1) and (-1 <= y <= 1)
    return result


otvet = IsPointInSquare(float(input()), float(input()))
if otvet:
    print('YES')
else:
    print('NO')
