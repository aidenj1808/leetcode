class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        a = 0
        b = 0
        counts = {x: 0 for x in range(1, len(grid) ** 2 + 1)}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                counts[grid[i][j]] += 1
        
        for num, count in counts.items():
            if count == 0:
                b = num
            elif count > 1:
                a = num
        return [a, b]
        
