class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        total += 1
        return total
        
