from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = Counter(stones)
        ret = 0
        for stone, count in counts.items():
            if stone in jewels:
                ret += count
        return ret
