class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ret = []
        for start, stop in zip(l, r):
            curr_subarray = sorted(nums[start: stop + 1])
            is_arithmetic = True
            for i in range(len(curr_subarray) - 1):
                if curr_subarray[i + 1] - curr_subarray[i] != curr_subarray[1] - curr_subarray[0]:
                    is_arithmetic = False
                    break
            ret.append(is_arithmetic)
        return ret

