from collections import Counter

class Solution:
    # Optimize
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        ret = []
        arr1_counts = Counter(arr1)
        for num in arr2:
            for _ in range(arr1_counts[num]):
                ret.append(num)
        
        ret2 = []
        for num, _ in arr1_counts.items():
            if num not in set(arr2):
                for _ in range(arr1_counts[num]):
                    ret2.append(num)
        return ret + sorted(ret2)
        
