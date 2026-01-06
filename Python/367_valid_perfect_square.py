class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        perfect_squares = [x ** 2 for x in range(1, 46341)]
        l = 0
        r = len(perfect_squares) - 1
        while l <= r:
            m = (l + r) // 2
            if num == perfect_squares[m]:
                return True
            elif num < perfect_squares[m]:
                r = m - 1
            else:
                l = m + 1
        return False

