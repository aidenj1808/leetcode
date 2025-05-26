class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words_and_order = [(word[: -1], word[-1]) for word in words]
        return " ".join([word for word, _ in sorted(words_and_order, key=lambda x: x[1])])

