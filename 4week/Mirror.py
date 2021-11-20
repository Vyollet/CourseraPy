def Mirror():
    n = int(input())
    if n != 0:
        Mirror()
        print(n)
    else:
        print(n)

Mirror()
