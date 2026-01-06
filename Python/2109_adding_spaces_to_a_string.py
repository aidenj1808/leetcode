class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        ret = ""
        cur_spaces_index = 0
        for i, char in enumerate(s):
            if cur_spaces_index < len(spaces) and i == spaces[cur_spaces_index]:
                ret += " " + char
                cur_spaces_index += 1
            else:
                ret += char
        return ret

