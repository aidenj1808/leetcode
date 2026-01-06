class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while -1 < i < len(num) and int(num[i]) % 2 == 0:
            i -= 1

        if i == -1:
            return ""
        return num[: i + 1]

