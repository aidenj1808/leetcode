class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        for start_value in range(1, 10000):
            total = start_value
            valid = 1
            for num in nums:
                total += num
                if total < 1:
                    valid = 0
                    break

            if valid:
                return start_value
        return -1

        # # Using min prefix sum: watch explanation video
        # minimum = total = 0
        # for num in nums:
        #     total += num
        #     minimum = min(s, m)
        # return 1 - minimum
            
