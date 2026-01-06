class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_1 = 0
        max_2 = 0
        for i in range(len(nums)):
            if nums[i] > max_1:
                max_2 = max_1
                max_1 = nums[i]
            elif nums[i] > max_2:
                max_2 = nums[i]
        return (max_1 - 1) * (max_2 - 1)

