import math
a, b, c = float(input()), float(input()), float(input())
p = (a + b + c) / 2
S = math.sqrt(p * (p - a) * (p - b) * (p - c))
if S % 2 == 0:
    print(int(S))
else:
    print('{0:.6f}'.format(S))
