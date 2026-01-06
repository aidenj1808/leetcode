from collections import Counter

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        counts = Counter(nums)
        total = 0
        for num, count in counts.items():
            if count == 1:
                total += num
        return total
        
