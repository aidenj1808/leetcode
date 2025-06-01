class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        evens = 0
        i = 0
        while i < len(nums) and evens < 2:
            if nums[i] % 2 == 0:
                evens += 1
            i += 1
        
        if evens == 2:
            return True
        return False

