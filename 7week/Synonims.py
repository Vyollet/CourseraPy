n = int(input())
sinon = {}
for i in range(0, n):
    p = list(map(str, input().split()))
    slov1, slov2 = p[0], p[1]
    sinon[slov1] = slov2
poisk = input()
if poisk in sinon:
    print(sinon[poisk])
else:
    for i in sinon:
        if sinon[i] == poisk:
            print(i)
