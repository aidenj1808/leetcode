class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        nums_set = set(nums)
        x = k
        while True:
            if x not in nums_set:
                return x
            x += k
    
