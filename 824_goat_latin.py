class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ret = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i, word in enumerate(sentence.split(), 1):
            if word[0].lower() in vowels:
                ret.append(word + "ma" + 'a' * i)
            else:
                ret.append(word[1:] + word[0] + "ma" + 'a' * i)
        return " ".join(ret)

