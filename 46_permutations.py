class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []

        def backtrack(i, current_perm):
            if i == n:
                res.append(current_perm[:])
                return

            for j in range(len(nums)):
                if nums[j] not in current_perm:
                    current_perm.append(nums[j])
                    backtrack(i + 1, current_perm)
                    current_perm.pop()

        backtrack(0, [])
        return res

