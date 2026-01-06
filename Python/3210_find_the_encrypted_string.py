class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ret = ""
        for i in range(len(s)):
            ret += s[(i + k) % len(s)]
        return ret

