class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        ret = set(nums)
        for num in nums:
            ret.add(int(str(num)[::-1]))
        return len(ret)

