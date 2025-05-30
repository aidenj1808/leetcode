class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        negative_count = 0
        postive_count = 0
        for num in nums:
            if num < 0:
                negative_count += 1
            elif num > 0:
                postive_count += 1
        return max(negative_count, postive_count)

