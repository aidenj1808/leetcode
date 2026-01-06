class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people = sorted(people)
        boats = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            boats += 1
        return boats

