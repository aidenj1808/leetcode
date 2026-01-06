class Solution:
    def transformArray(self, nums: list[int]) -> list[int]:
        ret_list = []
        for num in nums:
            if num % 2 == 0:
                ret_list.append(0)
            else:
                ret_list.append(1)
        return sorted(ret_list)
