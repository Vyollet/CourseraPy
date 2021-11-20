def CountSort(number):
    b = max(number) + 1
    poradok = [0] * b
    for now in number:
        poradok[now] += 1
    for n in range(len(poradok)):
        if poradok[n] >= 1:
            print((str(n) + ' ') * poradok[n], end='')

A = list(map(int, input().split()))
CountSort(A)
