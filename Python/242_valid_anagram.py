from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = Counter(s)
        t_counts = Counter(t)
        
        for char, count in s_counts.items():
            if char not in t_counts:
                return False
            elif t_counts[char] != count:
                return False

        for char, count in t_counts.items():
            if char not in s_counts:
                return False
            elif s_counts[char] != count:
                return False

        return True
        
