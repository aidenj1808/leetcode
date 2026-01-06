class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        cur_sum = 0
        ret_list = []
        for num in nums:
            ret_list.append(cur_sum + num)
            cur_sum += num
        return ret_list
        
