n = int(input())
max = 0
kolvo = 0
while n != 0:
    if n > max:
        max = n
        kolvo = 1
    elif n == max:
        kolvo += 1
    n = int(input())
print(kolvo)
