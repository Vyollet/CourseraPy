fin = open('input.txt', 'r', encoding='utf8')
f = fin.read().split()
wokabl = {}
for line in f:
    wordList = list(line.split(' '))
    for word in wordList:
        sWord = word.strip()
        wokabl[sWord] = wokabl.get(sWord, 0) + 1
for c in sorted(sorted(wokabl), key=wokabl.get, reverse=True):
    print(c)
    break
