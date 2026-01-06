from collections import Counter

class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        counts = Counter(nums)
        for _, count in counts.items():
            if count % 2 != 0:
                return False
        return True
        
