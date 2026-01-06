class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                ret += nums[i]
            else:
                ret -= nums[i]
        return ret
        
