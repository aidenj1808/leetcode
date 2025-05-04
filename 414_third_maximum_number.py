class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        distinct_nums = set(nums)
        distinct_nums_sorted = sorted(list(distinct_nums))
        if len(distinct_nums_sorted) > 2:
            return distinct_nums_sorted[-3]
        else:
            return distinct_nums_sorted[-1]
        
