class Solution:
    # Optimize with hashmap
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        pairs = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] == words[j][::-1]:
                    pairs += 1
        return pairs

