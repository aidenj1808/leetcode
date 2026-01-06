class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        ret = 0
        valid = 1
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if not 0 <= i < j < k < len(arr):
                        valid = 0
                    elif not abs(arr[i] - arr[j]) <= a:
                        valid = 0
                    elif not abs(arr[j] - arr[k]) <= b:
                        valid = 0
                    elif not abs(arr[i] - arr[k]) <= c:
                        valid = 0

                    if valid:
                        ret += 1
                    valid = 1
        return ret

