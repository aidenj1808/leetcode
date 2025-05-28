class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        ret = []
        for i in range(0, len(nums), 2):
            ret = ret + [nums[i + 1]] * nums[i]
        return ret

