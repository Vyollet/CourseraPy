str = input()
pos = str.find('f')
k = 0
while pos != -1:
    k += 1
    if k == 2:
        print(pos)
    pos = str.find('f', pos + 1)
if k == 0:
    print('-2')
if k == 1:
    print('-1')
