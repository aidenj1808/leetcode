class Solution:
    def stringHash(self, s: str, k: int) -> str:
        ret = ""
        for i in range(0, len(s), k):
            total = 0
            for j in range(k):
                total += ord(s[i + j]) - 97
            total %= 26
            ret += chr(total + 97)
        return ret

