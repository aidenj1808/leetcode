from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_count = 0
        ret = 0
        for num, count in counts.items():
            if count > max_count:
                max_count = count
                ret = num
        return ret

