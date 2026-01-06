class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        ret = []
        for i in range(len(nums)):
            suffix = nums[i + 1:]
            prefix = nums[: i + 1]
            ret.append(len(set(prefix)) - len(set(suffix)))
        return ret
        
