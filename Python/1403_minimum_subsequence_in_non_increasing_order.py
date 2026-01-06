class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums_sorted = sorted(nums, reverse=True)
        ret = []
        left_sum = 0
        right_sum = sum(nums)

        for num in nums_sorted:
            ret.append(num)
            left_sum += num
            right_sum -= num

            if left_sum > right_sum:
                break

        return ret

