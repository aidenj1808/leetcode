from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority_time = len(nums) // 2
        counts = Counter(nums)
        for num, count in counts.items():
            if count > majority_time:
                return num
        return -1
        
