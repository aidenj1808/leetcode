class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ret = [0] * n
        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                val = nums[left] ** 2
                left += 1
            else:
                val = nums[right] ** 2
                right -= 1
            ret[i] = val
        return ret

