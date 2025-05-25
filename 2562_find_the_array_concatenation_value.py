class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        ret = 0
        while left <= right:
            if left == right:
                ret += nums[left]
            else:
                ret += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        return ret

