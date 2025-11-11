from collections import Counter


class Solution:
    def sumDivisibleByK(self, nums: list[int], k: int) -> int:
        ret = 0
        counts = Counter(nums)
        for num, count in counts.items():
            if count % k == 0:
                ret += num * count
        return ret

