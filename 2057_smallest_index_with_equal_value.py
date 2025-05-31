class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        ret = -1
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                ret = i
                break
        return ret

