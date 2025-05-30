class Solution:
    # TC: O(n log n), optimize to O(n)
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sorted(nums, key=lambda x: (x % 2 == 1, x % 2 == 0))

