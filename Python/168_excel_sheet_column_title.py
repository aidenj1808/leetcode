class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret = ""
        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            ret = chr(ord('A') + offset) + ret
            columnNumber = (columnNumber - 1) // 26
        return ret

