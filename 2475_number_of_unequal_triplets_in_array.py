class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[i] == nums[k] or nums[j] == nums[k]:
                        continue
                    ret += 1
        return ret

