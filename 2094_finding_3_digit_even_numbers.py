from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        valid_digits = []
        digit_counts = Counter(digits)
        for i in range(100, 1000, 2):
            i_digit_counts = Counter(str(i))
            valid_digit = True
            for digit, count in i_digit_counts.items():     
                if digit_counts[int(digit)] < count:
                    valid_digit = False
            
            if valid_digit:
                valid_digits.append(i)
        return valid_digits

