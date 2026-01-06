class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        ret = float("-inf")
        while left <= right:
            ret = max(ret, nums[left] + nums[right])
            left += 1
            right -= 1
        return ret
    
