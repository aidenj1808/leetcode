class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        seen = set()
        ret_list = []
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                ret_list.append(num)
        return ret_list
