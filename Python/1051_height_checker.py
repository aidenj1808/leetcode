class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        heights_sorted = sorted(heights)
        count = 0
        for height, height_sorted in zip(heights, heights_sorted):
            if height != height_sorted:
                count += 1
        return count

