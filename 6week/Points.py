fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')
kolMest = int(fin.readline())
kolProshed = 0
obSum = []
for line in fin:
    line = line.split()
    a = int(line[-1])
    b = int(line[-2])
    c = int(line[-3])
    if (a >= 40) and (b >= 40) and (c >= 40):
        sum = a + b + c
        obSum.append(sum)
        kolProshed += 1
obSum.sort(reverse=True)
if obSum.count(obSum[0]) > kolMest:
    print(1, file=fout)
elif kolProshed <= kolMest:
    print(0, file=fout)
else:
    o = 0
    k = 0
    prohBal = 0
    while o == 0:
        o = obSum[kolMest-(k+1)] - obSum[kolMest-k]
        prohBal = obSum[kolMest-(k+1)]
        k += 1
    print(prohBal, file=fout)
fout.close()
fin.close()
