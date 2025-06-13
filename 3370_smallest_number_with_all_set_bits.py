class Solution:
    def smallestNumber(self, n: int) -> int:
        if n == 1:
            return 1

        b = 1
        while b <= n:
            b *= 2
        return b - 1

