from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        balloon = "balloon"
        for char in text:
            if char in balloon:
                counts[char] += 1
        
        if not all(char in counts for char in balloon):
            return 0
        return min(counts['b'], counts['a'], counts['l'] // 2, counts['o'] // 2, counts['n'])

