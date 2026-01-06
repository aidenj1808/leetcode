class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        ret = float("inf")
        left = 0
        right = len(nums) - 1
        nums = sorted(nums)
        while left < right:
            ret = min(ret, (nums[left] + nums[right]) / 2)
            left += 1
            right -= 1
        return ret
        
