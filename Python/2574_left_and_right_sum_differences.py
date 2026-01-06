class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        left_sum = [0]
        left_cur_sum = 0
        for i in range(len(nums) - 1):
            left_cur_sum += nums[i]
            left_sum.append(left_cur_sum)

        right_sum = [0]
        right_cur_sum = 0
        for i in range(len(nums) - 1, 0, -1):
            right_cur_sum += nums[i]
            right_sum.append(right_cur_sum)
        right_sum = right_sum[::-1]

        return [abs(left_num - right_num) for left_num, right_num in zip(left_sum, right_sum)]
        
