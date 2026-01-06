class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0

        ret = ""
        i = 0
        if s[0] == '-':
            ret += '-'
            i += 1
        elif s[0] == '+':
            ret += '+'
            i += 1

        while i < len(s) and s[i].isdigit():
            ret += s[i]
            i += 1

        ret = int(ret) if ret != '-' and ret != '+' and ret != '' else 0

        if ret > 2 ** 31 - 1:
            return 2 ** 31 - 1

        if ret <= -2 ** 31:
            return -2 ** 31
        
        return ret

