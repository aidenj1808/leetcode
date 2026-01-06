class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        operations = 0
        for i in range(1, len(nums)):
            new_num = max(nums[i - 1] + 1, nums[i])
            operations += abs(new_num - nums[i])
            nums[i] = new_num
        return operations
        
