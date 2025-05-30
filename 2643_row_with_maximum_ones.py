class Solution:
    def rowAndMaximumOnes(self, mat: list[list[int]]) -> list[int]:
        max_count = 0
        max_row = 0
        for i, row in enumerate(mat):
            row_sum = sum(row)
            if row_sum > max_count:
                max_count = row_sum
                max_row = i
        return [max_row, max_count]

