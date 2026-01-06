class Solution:
    def reverseWords(self, s: str) -> str:
        ret = [word[::-1] for word in s.split()]
        return " ".join(ret)
        
