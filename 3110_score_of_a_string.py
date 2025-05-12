class Solution:
    def scoreOfString(self, s: str) -> int:
        ret = 0
        for i in range(1, len(s)):
            ord_char1 = ord(s[i - 1])
            ord_char2 = ord(s[i])
            ret += abs(ord_char1 - ord_char2)
        return ret
        
