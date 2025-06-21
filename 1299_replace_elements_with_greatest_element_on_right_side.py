class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        current_max = -1
        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            arr[i] = current_max
            current_max = max(current_max, num)
        return arr

