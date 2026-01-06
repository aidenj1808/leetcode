class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums = sorted(nums, reverse=True)
        arr = []
        while len(nums) != 0:
            alice = nums.pop()
            bob = nums.pop()
            arr.append(bob)
            arr.append(alice)
        return arr
        
