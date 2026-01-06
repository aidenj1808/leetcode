class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        max_row = 0
        strongest = 0
        for i, row in enumerate(grid):
            row_sum = sum(row)
            if row_sum > max_row:
                max_row = row_sum
                strongest = i
        return strongest

