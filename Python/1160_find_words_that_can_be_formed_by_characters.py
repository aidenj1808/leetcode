from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_counts = Counter(chars)
        ret = 0
        for word in words:
            word_counts = Counter(word)
            valid = True
            for char, count in word_counts.items():
                if char not in char_counts:
                    valid = False
                elif char_counts[char] < count:
                    valid = False
            
            if valid:
                ret += len(word)
        return ret
        
