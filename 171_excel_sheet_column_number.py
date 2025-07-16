class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        n = len(columnTitle) - 1
        for i, char in enumerate(columnTitle):
            ret += (ord(char) - 64) * (26 ** (n - i))
        return ret

