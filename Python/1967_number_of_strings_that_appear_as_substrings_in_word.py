class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        ret = 0
        for pattern in patterns:
            if pattern in word:
                ret += 1
        return ret
        
