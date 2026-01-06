class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colour_counts = {}
        for num in nums:
            if num not in colour_counts:
                colour_counts[num] = 0
            colour_counts[num] += 1
        
        i = 0
        for colour, count in sorted(colour_counts.items(), key=lambda x: x[0]):
            for _ in range(count):
                nums[i] = colour
                i += 1

