class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        target_set = set(target)
        for num in arr:
            if num not in target_set:
                return False
        return sorted(arr) == sorted(target)

