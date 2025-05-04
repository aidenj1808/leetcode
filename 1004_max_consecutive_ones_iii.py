class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        zeros = 0
        left = 0
        max_consecutive_ones = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            window_size = right - left + 1
            max_consecutive_ones = max(max_consecutive_ones, window_size)
        return max_consecutive_ones

