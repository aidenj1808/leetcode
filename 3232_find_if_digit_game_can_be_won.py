class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        single_digits_sum = sum([num for num in nums if len(str(num)) == 1])
        double_digits_sum = sum([num for num in nums if len(str(num)) == 2])
        return single_digits_sum != double_digits_sum

