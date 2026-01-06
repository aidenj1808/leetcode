class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        count = 0
        ret_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            ret_list.append(count)
            count = 0
        return ret_list
        
