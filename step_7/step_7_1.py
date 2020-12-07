import numpy as np


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):

        ge = self.matrix
        gp = other.matrix
        qw = np.array(ge)
        wq = np.array(gp)
        return qw + wq

    #     matrix_sum = []
    #
    #         for i in range(len(self.matrix)):
    #             for y in range(len(self.matrix[0])):
    #                 matrix_sum[i][y] = self.matrix[i][y] + other.matrix[i][y]
    #         return matrix_sum
    #
    #



c = [
    [2, 3, 6],
    [5, 6, 8],
    [9, 7, 0]
]

q = [
    [2, 3, 4],
    [5, 4, 2],
    [1, 3, 10]
]

mc = Matrix(c)
mc2 = Matrix(q)

print(mc + mc2)

# print(mc, sep='],')
