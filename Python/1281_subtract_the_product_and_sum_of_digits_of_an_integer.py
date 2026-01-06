class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        for digit in str(n):
            digit = int(digit)
            product *= digit
            total += digit
        return product - total

