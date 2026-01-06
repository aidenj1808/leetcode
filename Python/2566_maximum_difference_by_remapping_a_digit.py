class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_string = str(num)
        if all([digit == '9' for digit in num_string]):
            return num
            
        non_nine = ""
        non_zero = ""
        i = 0
        while not (non_nine and non_zero):
            if num_string[i] != '9' and not non_nine:
                non_nine = num_string[i]
            
            if num_string[i] != '0' and not non_zero:
                non_zero = num_string[i]
            i += 1

        return int(num_string.replace(non_nine, '9')) - int(num_string.replace(non_zero, '0'))

