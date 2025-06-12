class Solution:
    def countBits(self, n: int) -> list[int]:
        return [f"{i:b}".count('1') for i in range(n + 1)]

