class Solution:
    def similarPairs(self, words: list[str]) -> int:
        ret = 0
        word_sets = [set(word) for word in words]
        for i in range(len(word_sets)):
            for j in range(i + 1, len(word_sets)):
                if word_sets[i] == word_sets[j]:
                    ret += 1
        return ret

