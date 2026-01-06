class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums = sorted(nums)
        i = 0
        while nums[i] < k:
            i += 1
        return i

