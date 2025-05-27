from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counts = Counter(arr)
        current_k = 0
        for char, count in counts.items():
            if count == 1:
                current_k += 1
            
            if current_k == k:
                return char
        return ''

