class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for x in range(n):
            total += x % 7 + x // 7 + 1
        return total

