class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        def vowels_in_s(s: str) -> int:
            vowels = ['a', 'e', 'i', 'o', 'u']
            vowels_count = 0
            for char in s:
                if char.lower() in vowels:
                    vowels_count += 1
            return vowels_count

        a = s[:len(s) // 2]
        b = s[len(s) // 2:]
        return vowels_in_s(a) == vowels_in_s(b)
        
