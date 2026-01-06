class Solution:
    def reverseDegree(self, s: str) -> int:
        ret = []
        for i in range(len(s)):
            ret.append((i + 1) * (26 - (ord(s[i]) - 97)))
        return sum(ret)

