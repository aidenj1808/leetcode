class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        def is_prefix_and_suffix(str1: str, str2: str) -> bool:
            str1_len = len(str1)
            if str2[: str1_len] == str1 and str2[len(str2) - str1_len:] == str1:
                return True
            return False

        ret = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if is_prefix_and_suffix(words[i], words[j]):
                    ret += 1
        return ret
        
