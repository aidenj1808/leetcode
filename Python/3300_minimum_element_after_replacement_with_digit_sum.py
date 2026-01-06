class Solution:
    def minElement(self, nums: list[int]) -> int:
        minn = float("inf")
        for num in nums:
            current_sum = 0
            for digit in str(num):
                current_sum += int(digit)
            minn = min(minn, current_sum)
        return minn

