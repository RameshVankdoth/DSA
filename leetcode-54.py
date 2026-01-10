import numpy as np

n = 5
mat = np.random.randint(0, 5, size=(n, n))

print(mat)
top, left, right, bottom = 0, 0, len(mat) - 1, len(mat[0]) - 1


while top <= bottom and left <= right:
    for i in range(left, right + 1):
        print(mat[top, i])
    top += 1

    for i in range(top, bottom + 1):
        print(mat[i, right])
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(mat[bottom, i])
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(mat[i, left])
        left += 1
