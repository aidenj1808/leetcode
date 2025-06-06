class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        search_word_len = len(searchWord)
        for i, word in enumerate(sentence.split(), 1):
            if word[:search_word_len] == searchWord:
                return i
        return -1

