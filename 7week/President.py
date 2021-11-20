fin = open('input.txt', 'r', encoding='utf8')
golos = 0
prezident = 0
keyList = []
fout = open('output.txt', 'w', encoding='utf8')
dicKandidat = {}
for kandidat in fin:
    stKandidat = kandidat.strip()
    dicKandidat[stKandidat] = dicKandidat.get(stKandidat, 0) + 1
    golos += 1
for c in sorted(dicKandidat, key=dicKandidat.get, reverse=True):
    if dicKandidat[c] > golos / 2:
        prezident += 1
        print(c, file=fout)
    else:
        keyList.append(c)
if prezident == 0:
    print(keyList[0], file=fout)
    print(keyList[1], file=fout)
fin.close()
fout.close()
