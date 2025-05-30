class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    ret += 1
        return ret
        
