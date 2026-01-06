class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        groups = len(s) // k
        ret = []
        for i in range(groups):
            ret.append(s[i * k: i * k + k])
        
        remainder = len(s) % k
        if remainder:
            ret.append(s[len(s) - remainder:] + fill * (k - remainder))
        return ret
        
