a, b, c = int(input()), int(input()), int(input())
k = 0
if (a == b) and (b == c):
    k = 3
elif (a == b) or (b == c) or (a == c):
    k = 2
else:
    k = 0
print(k)
