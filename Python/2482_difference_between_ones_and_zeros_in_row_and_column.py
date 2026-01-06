class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        diff = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ones_in_rows = [0] * len(grid)
        ones_in_cols = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones_in_rows[i] += 1
                    ones_in_cols[j] += 1
        
        for i in range(len(diff)):
            for j in range(len(diff[0])):
                diff[i][j] += ones_in_rows[i]
                diff[i][j] += ones_in_cols[j]
                diff[i][j] -= abs(ones_in_rows[i] - len(ones_in_cols))
                diff[i][j] -= abs(ones_in_cols[j] - len(ones_in_rows))
        return diff
                
