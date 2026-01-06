class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        for word_or_num in s.split():
            if word_or_num.isdigit() and int(word_or_num) <= prev:
                return False
            elif word_or_num.isdigit():
                prev = int(word_or_num)
        return True

