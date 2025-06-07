from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        counts = Counter(s)
        ret = ""
        while not all(val == 0 for val in counts.values()):
            for i in range(26):
                char = chr(97 + i)
                if counts[char] > 0:
                    ret += char
                    counts[char] -= 1
            
            for i in range(26):
                char = chr(122 - i)
                if counts[char] > 0:
                    ret += char
                    counts[char] -= 1
        return ret
                
