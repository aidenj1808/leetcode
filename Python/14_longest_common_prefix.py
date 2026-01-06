class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        p = 0
        min_length = min(len(word) for word in strs)
        ret = ""
        while p < min_length:
            current_char = strs[0][p]
            for word in strs[1:]:
                if word[p] != current_char:
                    return ret
            ret += current_char
            p += 1
        return ret

