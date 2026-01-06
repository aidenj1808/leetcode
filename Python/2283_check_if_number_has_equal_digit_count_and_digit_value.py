from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(num)
        for i in range(len(num)):
            if num[i] != str(counts[str(i)]):
                return False
        return True
        
