class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        ret = []
        for i in range(len(positives)):
            ret.append(positives[i])
            ret.append(negatives[i])
        return ret
        
