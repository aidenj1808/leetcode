class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        ret = []
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        row_mins = [float("inf") for _ in range(n_rows)]
        col_maxs = [float("-inf") for _ in range(n_cols)]

        for i in range(n_rows):
            for j in range(n_cols):
                row_mins[i] = min(row_mins[i], matrix[i][j])
                col_maxs[j] = max(col_maxs[j], matrix[i][j])

        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]:
                    ret.append(matrix[i][j])
        return ret

