class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing = []
        num = 1
        while len(missing) != k:
            if num not in arr:
                missing.append(num)
            num += 1
        return missing[-1]

