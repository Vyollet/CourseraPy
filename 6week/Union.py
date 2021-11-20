def merge(a1, b1):
    c = []
    i, j = 0, 0
    while len(c) < (len(a1) + len(b1)):
        if i >= len(a1):
            c.append(b1[j])
            j += 1
        elif j >= len(b1):
            c.append(a1[i])
            i += 1
        elif a1[i] >= b1[j]:
            c.append(b1[j])
            j += 1
        else:
            c.append(a1[i])
            i += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*(merge(a, b)))
