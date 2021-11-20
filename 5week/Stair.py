n = int(input())
k = 1
while n + 1 != k:
    for i in range(1, k + 1):
        print(i, end='', sep='')
    print('\n', end='')
    k += 1
