a,b,c,d,e,f = (float(input()) for _ in range(6))
dd = (a * d) - (c * b)
dx = (e * d) - (f * b)
dy = (a * f) - (e * c)
x = dx / dd
y = dy / dd
print(x, y)
