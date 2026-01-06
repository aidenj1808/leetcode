from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for char in ransomNote:
            if c[char] > 0:
                c[char] -= 1
            else:
                return False
        return True
        
