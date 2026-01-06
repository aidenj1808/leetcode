class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        max_num = max(nums)
        ret = 0
        for x in range(max_num, max_num + k):
            ret += x
        return ret
        
