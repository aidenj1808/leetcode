class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i, char in enumerate(s):
            total += abs(i - t.index(char))
        return total

