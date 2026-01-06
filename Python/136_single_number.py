class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ret = 0
        for num in nums:
            ret = ret ^ num
        return ret
        
