class Solution:
    def freqAlphabets(self, s: str) -> str:
        ret = ""
        i = len(s) - 1
        while 0 <= i < len(s):
            if s[i] == '#':
                ret = chr(int(s[i - 2: i]) + 96) + ret
                i -= 3
            else:
                ret = chr(int(s[i]) + 96) + ret
                i -= 1
        return ret

