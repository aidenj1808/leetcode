class Solution:
    def greatestLetter(self, s: str) -> str:
        seen = set(s)
        for x in range(26):
            char = chr(90 - x)
            if char in seen and char.lower() in seen:
                return char
        return ''
        
