class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ret = ""
        cipher = {}
        current_letter = 97
        seen = set()
        for char in key:
            if char not in seen and char != ' ':
                cipher.update({char: chr(current_letter)})
                current_letter += 1
                seen.add(char)
        cipher.update({' ': ' '})
        
        for char in message:
            ret += cipher[char]
        return ret
        
