class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        counts = {}
        for word in words:
            for char in word:
                if char not in counts:
                    counts[char] = 0
                counts[char] += 1
        
        for _, count in counts.items():
            if count % len(words) != 0:
                return False
        return True

