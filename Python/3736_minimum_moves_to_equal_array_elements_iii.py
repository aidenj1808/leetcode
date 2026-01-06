class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maxx = max(nums)
        total_moves = 0
        for num in nums:
            total_moves += abs(num - maxx)
        return total_moves

