class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        subarray_sums = []
        for i in range(len(nums) - 1):
            subarray_sums.append(nums[i] + nums[i + 1])
        return len(subarray_sums) != len(set(subarray_sums))

