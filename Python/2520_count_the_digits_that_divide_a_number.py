class Solution:
    def countDigits(self, num: int) -> int:
        ret = 0
        for digit in str(num):
            if num % int(digit) == 0:
                ret += 1
        return ret
        
