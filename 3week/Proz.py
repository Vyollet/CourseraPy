import math
p, x, y = float(input()), float(input()), float(input())
k = y / 100
vklad = x + k
vklad = vklad + ((vklad / 100) * p)
cel = math.floor(vklad)
kop = (int(vklad * 100)) % 100
print(cel, kop)
