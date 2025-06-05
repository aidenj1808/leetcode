class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            current_num = ""
            for i in range(1, len(s)):
                current_num += str((int(s[i - 1]) + int(s[i])) % 10)
            s = current_num
            
        if s[0] == s[1]:
            return True
        return False

