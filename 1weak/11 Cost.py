a, cop, n = [int(input()) for i in range(3)]
rub = a * 100
cost = sum([rub, cop])
total = cost * n
rub = total // 100
cop = total % 100
print(rub, cop)
