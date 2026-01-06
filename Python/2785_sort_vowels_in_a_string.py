class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels_in_s = [char for char in s if char.lower() in vowels]
        vowels_in_s = sorted(vowels_in_s)
        j = 0
        s_list = list(s)
        for i, char in enumerate(s):
            if char.lower() in vowels:
                s_list[i] = vowels_in_s[j]
                j += 1
        return "".join(s_list)

