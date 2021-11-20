vved = int(input())
pred = 0
kolvo = kolvo2 = 1
while vved != 0:
    if vved == pred:
        kolvo += 1
        if (kolvo > kolvo2):
            kolvo2 = kolvo
    else:
        kolvo = 1
        pred = vved
    vved = int(input())
print(kolvo2)
