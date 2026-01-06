class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        minn = min(nums)
        maxx = max(nums)
        for num in nums:
            if num != minn and num != maxx:
                return num
        return -1
        
