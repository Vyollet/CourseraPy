fin = open('input.txt', 'r', encoding='utf8')
abs = set()
for line in fin:
    line = line.split()
    for j in range(0, len(line)):
        abs.add(line[j])
print(len(abs))
fin.close()
