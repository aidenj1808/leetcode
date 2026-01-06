class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        operations = 0
        for num in nums:
            if num % 3 == 0:
                continue
            elif (num - 1) % 3 == 0:
                operations += 1
            elif (num + 1) % 3 == 0:
                operations += 1
        return operations
        
