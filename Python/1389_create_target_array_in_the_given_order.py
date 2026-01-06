class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        ret = []
        for num, i in zip(nums, index):
            ret.insert(i, num)
        return ret
        
