class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique_candies = set(candyType)
        can_eat = len(candyType) // 2

        if len(unique_candies) <= can_eat:
            return len(unique_candies)
        return can_eat

