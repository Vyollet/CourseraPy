def sum(a, b):
    if b != 0:
        a += 1
        b -= 1
        return (sum(a, b))
    else:
        return a


one = int(input())
two = int(input())
print(sum(one, two))
