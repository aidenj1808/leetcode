class Solution:
    # Optimize
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        max_bitwise_or = 0
        for num in nums:
            max_bitwise_or |= num

        n = len(nums)
        sol, ret = [], []
        def backtrack(i):
            if i == n:
                cur_bitwise_or = 0
                for num in sol:
                    cur_bitwise_or |= num

                if cur_bitwise_or == max_bitwise_or:
                    ret.append(1)   
                return

            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return sum(ret)

