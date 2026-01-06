class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        counts = {}
        for value, weight in items1 + items2:
            if value not in counts:
                counts[value] = 0
            counts[value] += weight
        return sorted(counts.items(), key=lambda x: x[0])
        
