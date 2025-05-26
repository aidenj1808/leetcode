class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == '':
            return []

        telephone_buttons = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z'], 
        }
        n = len(digits)
        res, sol = [], []
        def backtrack(i):
            if i == n:
                res.append("".join(sol))
                return
            
            for letter in telephone_buttons[digits[i]]:
                sol.append(letter)
                backtrack(i + 1)
                sol.pop()

        backtrack(0)
        return res
            
