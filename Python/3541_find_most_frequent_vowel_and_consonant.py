from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = Counter(s)
        vowel_max = 0
        con_max = 0
        for letter, count in counts.items():
            if letter in ['a', 'e', 'i', 'o', 'u'] and count > vowel_max:
                vowel_max = count
            elif letter not in ['a', 'e', 'i', 'o', 'u'] and count > con_max:
                con_max = count
        return vowel_max + con_max

