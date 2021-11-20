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

    def __add__(self, other):
        result = [[int(self.sList[y][x]) + int(other.sList[y][x])
                   for x in range(len(self.sList[0]))]
                  for y in range(len(self.sList))]
        return Matrix(result)

    def __mul__(self, other):
        result = [[int(self.sList[y][x]) * other
                   for x in range(len(self.sList[0]))]
                  for y in range(len(self.sList))]
        return Matrix(result)

    def __rmul__(self, other):
        return Matrix.__mul__(self, other)

m = Matrix([[1, 1, 0], [0,2,10], [10,15,30]])
alpha = 15
print(m * alpha)
print(alpha * m)