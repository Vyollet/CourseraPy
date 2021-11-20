str = input()
while str.find('@') != -1:
    str = str.replace('@', '')
print(str)
