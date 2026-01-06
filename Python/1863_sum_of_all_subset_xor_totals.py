class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                xor_total = 0
                for i in range(len(sol)):
                    xor_total = xor_total ^ sol[i]
                res.append(xor_total)
                return

            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return sum(res)

