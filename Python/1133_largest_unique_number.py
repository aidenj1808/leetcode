from collections import Counter

class Solution:
    def largestUniqueNumber(self, nums: list[int]):
        num_counts = Counter(nums)
        ret = -1
        for num, count in num_counts.items():
            if count == 1:
                ret = max(ret, num)
        return ret

