from collections import Counter

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        words1_counts = Counter(words1)
        words2_counts = {}
        for word in words2:
            if word not in words2_counts and word in words1_counts:
                words2_counts[word] = 0

            if word in words1_counts:
                words2_counts[word] += 1

        ret = 0
        for word, count in words1_counts.items():
            if word in words2_counts and count == 1 and words2_counts[word] == 1:
                ret += 1
        return ret

