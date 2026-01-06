class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        valid = 1
        for word in words:
            for char in word:
                if char not in allowed:
                    valid = 0
            if valid:
                count += 1
            valid = 1
        return count

