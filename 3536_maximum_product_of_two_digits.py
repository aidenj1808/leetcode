class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted(int(x) for x in str(n))
        return digits[-1] * digits[-2]
        
