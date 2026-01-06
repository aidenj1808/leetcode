class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 0
        current_line = 0
        for char in s:
            width = widths[ord(char) - 97]
            if current_line + width > 100:
                lines += 1
                current_line = width
            else:
                current_line += width
        return [lines + 1, current_line]

