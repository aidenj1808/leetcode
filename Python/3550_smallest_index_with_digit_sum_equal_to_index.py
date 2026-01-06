class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            current_sum = 0
            for digit in str(nums[i]):
                current_sum += int(digit)
            
            if current_sum == i:
                return i
        return -1
        
