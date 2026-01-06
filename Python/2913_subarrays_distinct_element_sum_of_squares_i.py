class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        distinct_counts = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                distinct_counts.append(len(set(nums[i: j + 1])))
        
        return sum([count ** 2 for count in distinct_counts])

