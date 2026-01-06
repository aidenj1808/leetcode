class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        ret = []
        for i in range(len(grid[0])):
            max_len = 0
            for j in range(len(grid)):
                max_len = max(max_len, len(str(grid[j][i])))
            ret.append(max_len)
        return ret

