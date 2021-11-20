import math
x = float(input())
cel = math.floor(x)
ost = x - cel
if ost < 0.5:
    print(math.floor(x))
else:
    print(math.ceil(x))
