class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr_sorted = sorted(arr)
        difference_expected = arr_sorted[1] - arr_sorted[0]
        for i in range(1, len(arr_sorted)):
            difference = arr_sorted[i] - arr_sorted[i - 1]
            if difference != difference_expected:
                return False
        return True

