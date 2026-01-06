class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        str_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u']
        while left <= right:
            if str_list[left].lower() in vowels and str_list[right].lower() in vowels:
                str_list[left], str_list[right] = str_list[right], str_list[left]
                left += 1
                right -= 1
            elif str_list[left].lower() in vowels:
                right -= 1
            else:
                left += 1
        return "".join(str_list)

