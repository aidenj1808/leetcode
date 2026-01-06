class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_num = int("".join([str(ord(digit) - 97) for digit in firstWord]))
        second_num = int("".join([str(ord(digit) - 97) for digit in secondWord]))
        target_num = int("".join([str(ord(digit) - 97) for digit in targetWord]))
        return first_num + second_num == target_num
        
