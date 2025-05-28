class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        operations = 0
        while operations < k:
            min_value = min(nums)
            i = nums.index(min_value)
            nums[i] = nums[i] * multiplier
            operations += 1
        return nums

