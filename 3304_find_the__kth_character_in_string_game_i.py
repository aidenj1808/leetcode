class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) < k:
            generated_string = ""
            for char in word:
                generated_string += chr((ord(char) + 1) % ord('z'))
            word += generated_string
        return word[k - 1]

