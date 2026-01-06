class Solution:
    def isPowerOfFour(self, n: int | float) -> bool:
        while n > 1:
            n /= 4
        if n < 1:
            return False
        return True
        
