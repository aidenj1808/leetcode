class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        capacity = sorted(capacity, reverse=True)
        total_apples = sum(apple)
        current_total = 0
        i = 0
        while current_total < total_apples:
            current_total += capacity[i]
            i += 1
        return i

