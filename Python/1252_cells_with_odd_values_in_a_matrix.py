class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        zero_matrix = [[0 for _ in range(n)] for _ in range(m)]
        for r, c in indices:
            for i in range(m):
                zero_matrix[i][c] += 1

            for i in range(n):
                zero_matrix[r][i] += 1
        
        count = 0
        for i in range(len(zero_matrix)):
            for j in range(len(zero_matrix[0])):
                if zero_matrix[i][j] % 2 == 1:
                    count += 1
        return count
        
