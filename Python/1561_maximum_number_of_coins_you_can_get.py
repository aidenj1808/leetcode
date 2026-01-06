class Solution:
    # Optimize
    def maxCoins(self, piles: list[int]) -> int:
        piles_sorted = sorted(piles)
        ret = 0
        while piles_sorted:
            piles_sorted.pop()
            ret += piles_sorted.pop()
            piles_sorted.pop(0)
        return ret

