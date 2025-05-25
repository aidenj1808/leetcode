class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        digits = [int(digit) for digit in str(n)]
        sum_of_squares = sum([digit ** 2 for digit in digits])
        while sum_of_squares not in seen:
            seen.add(sum_of_squares)
            if sum_of_squares == 1:
                return True

            digits = [int(digit) for digit in str(sum_of_squares)]
            sum_of_squares = sum([digit ** 2 for digit in digits])    
        return False

