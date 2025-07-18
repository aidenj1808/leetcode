class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                matches += n
            else:
                n = n // 2 + 1
                matches += n - 1
        return matches

