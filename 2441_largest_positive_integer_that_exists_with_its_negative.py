class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        ret = 0
        nums_set = set(nums)
        for num in nums:
            if num * -1 in nums_set:
                ret = max(ret, num)
        if ret:
            return ret
        return -1
        
