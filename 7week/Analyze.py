fin = open('input.txt', 'r', encoding='utf8')
f = fin.read().split()
wokabl = {}
for line in f:
    wordList = list(line.split(' '))
    for word in wordList:
        sWord = word.strip()
        wokabl[sWord] = wokabl.get(sWord, 0) + 1
listWord = []
for c in sorted(wokabl):
    listWord.append([wokabl[c], c])
listWord.sort(key=lambda p: p[1])
listWord.sort(key=lambda p: p[0], reverse=True)
for i in range(0, len(listWord)):
    print(listWord[i][1])
