fin = open('input.txt', 'r', encoding='utf8')
f = fin.read().split()
myDic = {}
otv = []
for line in f:
    wordList = list(line.split(' '))
    for word in wordList:
        sWord = word.strip()
        if (sWord) not in myDic:
            myDic[sWord] = 0
        else:
            myDic[sWord] += 1
        otv.append(myDic[sWord])
print(*otv)
