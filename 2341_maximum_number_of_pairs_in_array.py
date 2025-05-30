from collections import Counter

class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        leftovers = 0
        counts = Counter(nums)
        for _, count in counts.items():
            if count % 2 == 1:
                leftovers += 1
        return [(len(nums) - leftovers) // 2, leftovers]
 
