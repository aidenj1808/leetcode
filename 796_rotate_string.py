class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for _ in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                return True
        return False
        
