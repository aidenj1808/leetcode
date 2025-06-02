class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        max_cols = []
        for col in range(len(matrix[0])):
            current_max = float("-inf")
            for row in range(len(matrix)):
                current_max = max(current_max, matrix[row][col])
            max_cols.append(current_max)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_cols[j]
        return matrix

