class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        ret = float("inf")
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if i == j: continue
                for k in range(j + 1, n):
                    if j == k: continue
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        ret = min(ret, nums[i] + nums[j] + nums[k])
                        
        if ret == float("inf"):
            return -1
        return ret

