class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        ret = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for word in words[left: right + 1]:
            if word[0] in vowels and word[-1] in vowels:
                ret += 1
        return ret

