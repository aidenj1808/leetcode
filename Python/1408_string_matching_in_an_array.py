class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        n = len(words)
        ret = set()
        for i in range(n):
            for j in range(i + 1, n):
                if words[i] in words[j]:
                    ret.add(words[i])
                
                if words[j] in words[i]:
                    ret.add(words[j])
        return list(ret)

