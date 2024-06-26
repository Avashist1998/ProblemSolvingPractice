from typing import List

def set_matrix_zeros(matrix: List[List[int]]) -> List[List[int]]:


    zero_rows = set()
    zero_cols = set()

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                zero_rows.add(i)
                zero_cols.add(j)


    for row in list(zero_rows):
        for j in range(len(matrix[0])):
            matrix[row][j] = 0
    
    for col in list(zero_cols):
        for i in range(len(matrix)):
            matrix[i][col] = 0
    
    return matrix