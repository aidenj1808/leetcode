class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        distinct_averages = set()
        while left <= right:
            remove_average = (nums[left] + nums[right]) / 2
            distinct_averages.add(remove_average)
            left += 1
            right -= 1
        return len(distinct_averages)
        
