class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) != 1:
            total = 0
            for digit in num_str:
                total += int(digit)
            num_str = str(total)
        return int(num_str)

