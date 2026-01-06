class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        special_nums = [nums[i] for i in range(len(nums)) if n % (i + 1) == 0]
        return sum([num ** 2 for num in special_nums])

