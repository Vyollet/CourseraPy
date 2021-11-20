from sys import stdin
import copy

class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

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
        if len(self.sList) == len(other.sList):
            result = [[int(self.sList[y][x]) + int(other.sList[y][x])
                       for x in range(len(self.sList[0]))]
                      for y in range(len(self.sList))]
            return Matrix(result)
        else:
            error = MatrixError(self, other)
            raise error

    def __mul__(self, other):
        result = [[int(self.sList[y][x]) * other
                   for x in range(len(self.sList[0]))]
                  for y in range(len(self.sList))]
        return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        self.sList = [[self.sList[y][x] for y in range(len(self.sList))]
                      for x in range(len(self.sList[0]))]
        return Matrix(self.sList)

    def transposed(self):
        result = [[self.sList[y][x] for y in range(len(self.sList))]
                  for x in range(len(self.sList[0]))]
        return Matrix(result)

m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
m1 = m.transpose()
print(m)
print(m1)
