class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                current_element = matrix[i][j]
                if i != 0 and j != 0 and matrix[i - 1][j - 1] != current_element:
                    return False
        return True

