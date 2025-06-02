class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        nums_sum = sum(nums)
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        
        for i in range(len(nums)):
            left_sum = prefix_sum[i] - nums[i]
            right_sum = nums_sum - prefix_sum[i]
            if left_sum == right_sum:
                return i
        return -1

