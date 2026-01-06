from collections import Counter

class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        ret = 0
        counts = Counter(nums)
        for num, count in counts.items():
            if count == 2:
                ret ^= num
        return ret

