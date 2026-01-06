class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        current_maxs = []
        ret = 0
        while len(grid[0]) != 0:
            for row in grid:
                max_num = max(row)
                current_maxs.append(max_num)
                row.remove(max_num)
            ret += max(current_maxs)
            current_maxs = []
        return ret

