class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        minn = min(nums)
        maxx = max(nums)
        ret = []
        for num in range(minn, maxx + 1):
            if num not in nums:
                ret.append(num)
        return ret

