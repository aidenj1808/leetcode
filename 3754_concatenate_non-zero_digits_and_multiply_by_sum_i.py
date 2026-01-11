class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum_x = 0
        x = "0"
        placement = 1
        for digit in str(n):
            if digit != '0':
                sum_x += int(digit)
                x += digit
                placement *= 10
        return sum_x * int(x)

