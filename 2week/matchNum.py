a, b, c = (int(input()) for _ in range(3))
i = 0
if a == b == c:
    i = 3
elif a == b or b == c or a == c:
    i = 2
print(i)