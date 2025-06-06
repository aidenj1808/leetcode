class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_num = ""
        for i in range(10):
            if str(i) * 3 in num:
                max_num = max(max_num, str(i))
        return max_num * 3

