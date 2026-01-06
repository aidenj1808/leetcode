class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and (i == j or i + j == len(grid) - 1):
                    return False
                elif grid[i][j] != 0 and not (i == j or i + j == len(grid) - 1):
                    return False
        return True

