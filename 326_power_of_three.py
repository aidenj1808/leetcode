class Solution:
    def isPowerOfThree(self, n: int | float) -> bool:
        while n > 1:
            n /= 3
        if n < 1:
            return False
        return True

