class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        ret = 0
        for word in words:
            word_len = len(word)
            if s[: word_len] == word:
                ret += 1
        return ret
            
