class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        size = 10
        ret = set()
        seen = set()
        for i in range(size, len(s) + 1):
            substring = s[i - size: i]
            if substring not in seen:
                seen.add(substring)
            else:
                ret.add(substring)      
        return list(ret)
    
