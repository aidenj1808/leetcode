class Solution:
    def sumZero(self, n: int) -> list[int]:
        ret = []
        for i in range(1, n // 2 + 1):
            ret.append(i)
            ret.append(-i)
        
        if n % 2 == 1:
            return ret + [0]
        return ret
        
