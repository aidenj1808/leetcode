class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        ret = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if (left_sum - right_sum) % 2 == 0:
                ret += 1
        return ret
            
