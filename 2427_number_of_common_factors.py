class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ret = 0
        for x in range(1, min(a, b) + 1):
            if a % x == 0 and b % x == 0:
                ret += 1
        return ret
        
