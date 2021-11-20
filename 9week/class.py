from sys import stdin
import copy 

class Matrix:
    def __init__(self, fList):
        self.sList = copy.deepcopy(fList)

    def __str__(self):
        rStr = ''
        for k in range(len(self.sList)):
            rStr += '\t'.join(map(str, self.sList[k])) + '\n'
        return rStr[:-1]

    def size(self):
        return len(self.sList), len(self.sList[0])

m1 = Matrix([[1,0,0], [1, 1, 1], [0, 0, 0]])
m2 = Matrix([[1,0,0], [1, 1, 1], [0, 0, 0]])
print(str(m1) == str(m2))
