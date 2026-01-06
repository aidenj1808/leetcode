class Solution:
    def specialArray(self, nums: list[int]) -> int:
        vals = [x for x in range(len(nums) + 1)]
        counts = {}
        for val in vals:
            if val not in counts:
                counts[val] = 0

            for num in nums:
                if num >= val:
                    counts[val] += 1
                       
        ret = -1
        for val, count in counts.items():
            if val == count:
                return val
        return ret

