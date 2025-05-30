class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        count = 0
        largest_square = float("-inf")
        for l, w in rectangles:
            square = min(l, w)
            if square > largest_square:
                largest_square = square
                count = 1
            elif square == largest_square:
                count += 1
        return count

