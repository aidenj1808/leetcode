from math import floor, sqrt

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        for _ in range(k):
            max_gifts = max(gifts)
            max_gifts_i = gifts.index(max_gifts)
            gifts[max_gifts_i] = floor(sqrt(gifts[max_gifts_i]))
        return sum(gifts)
        
