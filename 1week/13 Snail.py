h,a,b = (int(input()) for _ in range(3))
day = ((h - a) + (a - b) - 1) // (a - b)
print(day + 1)
