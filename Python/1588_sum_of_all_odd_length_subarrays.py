class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        ret = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarray = arr[i: j + 1]
                if len(subarray) % 2 == 1:
                    ret += sum(subarray)
        return ret
        
