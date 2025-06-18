class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr = sorted(arr)
        shortened_arr = arr[int(len(arr) * 0.05): int(len(arr) * 0.95)]
        return sum(shortened_arr) / len(shortened_arr)

