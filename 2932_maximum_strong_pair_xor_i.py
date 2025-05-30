class Solution:
    def maximumStrongPairXor(self, nums: list[int]) -> int:
        max_xor = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor

