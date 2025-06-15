class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ret = []
        for x in range(left, right + 1):
            valid = True
            x_str = str(x)
            i = 0
            while valid and i < len(x_str):
                if x_str[i] == '0' or x % int(x_str[i]) != 0:
                    valid = False
                i += 1
            
            if valid:
                ret.append(x)
        return ret

