class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            ret += sum(nums[start: i + 1])
        return ret
        
