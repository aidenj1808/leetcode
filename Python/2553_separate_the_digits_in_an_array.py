class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ret = []
        num_strings = [str(num) for num in nums]
        for num in num_strings:
            for digit in num:
                ret.append(int(digit))
        return ret
        
