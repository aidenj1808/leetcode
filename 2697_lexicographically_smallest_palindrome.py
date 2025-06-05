class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s_list = list(s)
        while left < right:
            if s_list[left] != s_list[right]:
                min_char = chr(min(ord(s_list[left]), ord(s_list[right])))
                s_list[left] = min_char
                s_list[right] = min_char
            left += 1
            right -= 1
        return "".join(s_list)

