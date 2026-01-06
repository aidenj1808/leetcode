class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr_sorted = sorted(arr)
        minn = float("inf")
        for i in range(len(arr_sorted) - 1):
            minn = min(minn, arr_sorted[i + 1] - arr_sorted[i])
        
        ret = []
        for i in range(len(arr_sorted) - 1):
            if arr_sorted[i + 1] - arr_sorted[i] == minn:
                ret.append([arr_sorted[i], arr_sorted[i + 1]])
        return ret

