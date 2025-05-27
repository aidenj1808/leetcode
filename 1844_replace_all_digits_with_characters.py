class Solution:
    def replaceDigits(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            if s[i].isalpha():
                ret += s[i]
            else:
                ret += chr(ord(s[i - 1]) + int(s[i]))
        return ret
        
