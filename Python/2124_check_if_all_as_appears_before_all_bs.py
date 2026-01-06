class Solution:
    def checkString(self, s: str) -> bool:
        a_i = float("-inf")
        b_i = float("inf")
        ret = True
        for i in range(len(s)):
            if s[i] == 'a':
                a_i = i
            elif s[i] == 'b':
                b_i = i

            if a_i > b_i:
                return False
        return ret

