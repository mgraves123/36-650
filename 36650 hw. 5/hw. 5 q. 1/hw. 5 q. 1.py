#https://www.javaexercise.com/python/python-list-of-lists

def transpose_mat(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_mat = []
    for c in range(cols):
        new_mat.append([])
    for i in range(rows):
        for j in range(cols):
            new_mat[j].append(matrix[i][j])
    for r in new_mat: 
        print(r)

(transpose_mat([[10, 8], [2, 4], [1, 7]]))