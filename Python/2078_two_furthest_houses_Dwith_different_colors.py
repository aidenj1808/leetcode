class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        left = 0
        right = len(colors) - 1
        max_distance = 0
        while left < right:
            if colors[left] != colors[right]:
                max_distance = max(max_distance, abs(left - right))
            right -= 1

        left = 0
        right = len(colors) - 1
        while left < right:
            if colors[left] != colors[right]:
                max_distance = max(max_distance, abs(left - right))
            left += 1

        return max_distance

