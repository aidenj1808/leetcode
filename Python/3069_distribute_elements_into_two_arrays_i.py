class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        ret1 = [nums[0]]
        ret2 = [nums[1]]
        for num in nums[2:]:
            if ret1[-1] > ret2[-1]:
                ret1.append(num)
            else:
                ret2.append(num)
        return ret1 + ret2
        
