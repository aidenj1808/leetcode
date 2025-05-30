class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total <= target:
                left += 1
            else:
                right -= 1

