from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        nums = [int(x) for x in str(n)]
        counts = Counter(nums).items()
        return sorted(counts, key = lambda counts: (counts[1], counts[0]))[0][0]

