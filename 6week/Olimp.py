fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
text = []
l = int(fin.readline())
for line in fin:
    line = line.split()
    a = (line[1], line[0])
    text.append(a)
text.sort(key=lambda x: int(x[0]), reverse=True)
for i in range(0, l):
    print(text[i][1], file=fout)
fout.close()
fin.close()
