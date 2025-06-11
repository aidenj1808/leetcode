class Solution:
    def maximum69Number (self, num: int | str) -> int:
        num = str(num)
        if num.count('9') == len(num):
            return int(num)
        
        i = 0
        while i < len(num) and num[i] == '9':
            i += 1
        return int(num[:i] + '9' + num[i + 1:])

