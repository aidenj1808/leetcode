class Solution:
    def makeFancyString(self, s: str) -> str:
        ret = ""
        current_char = ""
        current_count = 0
        for char in s:
            if char != current_char:
                current_char = char
                current_count = 0
            current_count += 1

            if current_count < 3:
                ret += current_char
        return ret
            
