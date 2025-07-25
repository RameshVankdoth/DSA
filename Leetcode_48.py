# import numpy as np

# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# x = np.array(mat)
# print(x.T)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(mat)):
    for j in range(i + 1, len(mat[i])):
        mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

print(mat)

p = len(mat) - 1
q = 0
while q <= p:
    mat[p], mat[q] = mat[q], mat[p]
    p -= 1
    q += 1

print(mat)
