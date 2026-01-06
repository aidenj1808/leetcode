class Solution:
    def maximizeExpressionOfThree(self, nums: list[int]) -> int:
        nums_sorted = sorted(nums)
        return nums_sorted[-1] + nums_sorted[-2] - nums_sorted[0]
        
