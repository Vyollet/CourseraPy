fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
text = []
l = 0
for line in fin:
    line = line.split()
    a = (line[0], line[1], line[2], line[3])
    text.append(a)
    l += 1
text.sort()
for i in range(0, l):
    print(text[i][0], end=' ', file=fout)
    print(text[i][1], end=' ', file=fout)
    print(text[i][3], file=fout)
fout.close()
fin.close()
