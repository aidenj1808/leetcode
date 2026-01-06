from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)
        return len(counts.keys()) == len(set(counts.values()))

