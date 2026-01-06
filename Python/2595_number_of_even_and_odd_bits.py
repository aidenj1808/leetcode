class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        evens = 0
        odds = 0
        for i, bit in enumerate(f"{n:b}"[::-1]):
            if i % 2 == 0 and bit == '1':
                evens += 1
            elif i % 2 == 1 and bit == '1':
                odds += 1
        return [evens, odds]

