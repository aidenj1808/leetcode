class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1_str = '0' * (4 - len(str(num1))) + str(num1)
        num2_str = '0' * (4 - len(str(num2))) + str(num2)
        num3_str = '0' * (4 - len(str(num3))) + str(num3)

        ret = ""
        for i in range(4):
            ret += str(min(int(num1_str[i]), int(num2_str[i]), int(num3_str[i])))
        return int(ret)

