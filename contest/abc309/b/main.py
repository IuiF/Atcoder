import numpy as np


def rotate_outer_clockwise(matrix):
    top = matrix[0, :]
    right = matrix[1:-1, -1]
    bottom = matrix[-1, ::-1]
    left = matrix[-2:0:-1, 0]
    outer = np.concatenate((top, right, bottom, left))
    outer = np.roll(outer, 1)
    matrix[0, :] = outer[: top.size]
    matrix[1:-1, -1] = outer[top.size : top.size + right.size]
    matrix[-1, :] = outer[top.size + right.size : top.size + right.size + bottom.size][
        ::-1
    ]
    matrix[-2:0:-1, 0] = outer[top.size + right.size + bottom.size :]
    return matrix


N = int(input())
arr = np.array([list(input()) for _ in range(N)])

arr = rotate_outer_clockwise(arr)

for r in arr:
    print(*r, sep="")
