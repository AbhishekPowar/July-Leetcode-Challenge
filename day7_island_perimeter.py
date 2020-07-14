mat = [[0, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 1, 0, 0],
       [1, 1, 0, 0]]
col_len = len(mat)
row_len = len(mat[0])

c = 0
for i in range(col_len):
    for j in range(row_len):
        if mat[i][j]:
            if i-1 < 0 or mat[i-1][j] == 0:
                c += 1
            if i+1 >= col_len or mat[i+1][j] == 0:
                c += 1
            if j-1 < 0 or mat[i][j-1] == 0:
                c += 1
            if j+1 >= row_len or mat[i][j+1] == 0:
                c += 1
