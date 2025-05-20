class Solution:
    # O(n * m), Optimize for better time complexity   
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ret = 0
        for i in range(len(arr1)):
            valid = 1
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    valid = 0
            if valid:
                ret += 1
        return ret

