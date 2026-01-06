class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        ret = set(nums[0])
        for num in nums[1:]:
            ret = ret & set(num)
        return sorted(list(ret))

