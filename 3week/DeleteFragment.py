str = input()
rts = str[::-1]
pos = str.find('h')
pos2 = (len(str) - 1 - (rts.find('h')))
print(str[:pos], str[pos2 + 1:], sep='')
