from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        counts = Counter(nums)
        current_max = float("-inf")
        current_total = 0
        for _, count in counts.items():
            if count > current_max:
                current_max = count
                current_total = count
            elif count == current_max:
                current_total += count
        return current_total
        
