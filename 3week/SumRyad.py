n = int(input())
s = 0
k = 1
while k <= n:
    s = s + (1 / (k ** 2))
    k += 1
if s % 2 == 0:
    print(int(s))
else:
    print('{0:.6f}'.format(s))
