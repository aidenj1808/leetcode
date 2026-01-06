class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and f"{n:b}".count('1') == 1

