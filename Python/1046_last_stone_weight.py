class Solution:
    # Optimize
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = sorted(stones)
        print(stones)
        while len(stones) > 1:
            stone1 = stones[-1]
            stone2 = stones[-2]
            if stone1 == stone2:
                stones.pop()
                stones.pop()
            else:
                stones.pop(-2)
                stones[-1] = stone1 - stone2
            stones = sorted(stones)
        
        if len(stones) == 0:
            return 0
        return stones[0]

