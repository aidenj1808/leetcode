from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        nums_freq = []
        print(counts)
        for num in nums:
            nums_freq.append((num, counts[num]))
        nums_freq_sorted = sorted(nums_freq, key = lambda x: x[0], reverse = True)
        nums_freq_sorted = sorted(nums_freq_sorted, key = lambda x: x[1])
        return [val for val, _ in nums_freq_sorted]
        
