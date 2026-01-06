class Solution:
    def minimumChairs(self, s: str) -> int:
        min_chairs = 0
        current_people = 0
        for char in s:
            if char == "E":
                current_people += 1
            elif char == "L":
                current_people -= 1
            min_chairs = max(min_chairs, current_people)
        return min_chairs

