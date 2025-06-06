class Solution:
    def arraySign(self, nums: list[int]) -> int:
        res = 1
        for num in nums:
            if num == 0:
                return 0
            elif num > 0:
                res *= 1
            else:
                res *= -1
                
        if res > 0:
            return 1
        return -1

