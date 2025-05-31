class Solution:
    def returnToBoundaryCount(self, nums: list[int]) -> int:
        location = 0
        ret = 0
        for num in nums:
            location += num
            if location == 0:
                ret += 1
        return ret
        
