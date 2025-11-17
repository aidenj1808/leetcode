class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        for x in str(n):
            digit_sum += int(x)
            digit_product *= int(x)

        total = digit_sum + digit_product
        return n % total == 0 and n % total == 0

