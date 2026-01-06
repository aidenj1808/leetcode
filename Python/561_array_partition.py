class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums_sorted = sorted(nums)
        ret = 0
        for i in range(0, len(nums_sorted) - 1, 2):
            ret += min(nums_sorted[i], nums_sorted[i + 1])
        return ret

