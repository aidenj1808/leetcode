from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        all_words = s1.split() + s2.split()
        counts = Counter(all_words)
        return [word for word, count in counts.items() if count == 1]

