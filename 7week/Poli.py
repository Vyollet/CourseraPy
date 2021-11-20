n = int(input())
lLanguage = []
for i in range(0, n):
    m = int(input())
    for j in range(0, m):
        lang = input()
        lLanguage.append(lang)
sLanguage = set(lLanguage)
znVse = []
for k in sLanguage:
    kolvo = lLanguage.count(k)
    if kolvo == n:
        znVse.append(k)
print(len(znVse))
for i in znVse:
    print(i)
print(len(sLanguage))
for i in sLanguage:
    print(i)
