str = input()
pos = str.find('f')
if pos != -1:
    print(pos, end=' ')
    if str.find('f', pos + 1) != -1:
        rts = str[::-1]
        pos2 = rts.find('f')
        print(len(str) - 1 - pos2)
