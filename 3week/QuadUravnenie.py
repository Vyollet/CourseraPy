import math
a, b, c = float(input()), float(input()), float(input())
d = (b ** 2) - (4 * a * c)
if int(d) >= 0:
    x1 = ((b * -1) - (d ** 0.5)) / (2 * a)
    x2 = ((b * -1) + (d ** 0.5)) / (2 * a)
    if x1 == x2:
        print(x1)
    else:
        print(min(x1, x2), max(x1, x2))
