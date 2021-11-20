import math
cena = float(input())
cel = math.floor(cena)
kop = '{0:.0f}'.format((cena - cel) * 100)
print(cel, kop)
