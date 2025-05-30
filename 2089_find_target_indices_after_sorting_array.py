class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ret = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if num == target:
                ret.append(i)
        return ret

