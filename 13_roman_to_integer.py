class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        subtract = 0
        for i in range(len(s) - 1, -1, -1):
            if roman_to_int[s[i - 1]] < roman_to_int[s[i]] and i != 0:
                total += roman_to_int[s[i]]
                subtract = 1
            elif subtract:
                total -= roman_to_int[s[i]]
                subtract = 0
            else:
                total += roman_to_int[s[i]]
        return total

