class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        ret = 0
        for i in range(len(nums)):
            if f"{i:b}".count("1") == k:
                ret += nums[i]
        return ret

