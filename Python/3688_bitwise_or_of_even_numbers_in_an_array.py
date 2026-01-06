class Solution:
    def evenNumberBitwiseORs(self, nums: list[int]) -> int:
        ret = 0
        for num in nums:
            if num % 2 == 0:
                ret |= num
        return ret

