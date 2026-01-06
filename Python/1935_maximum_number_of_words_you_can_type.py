class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ret = 0
        for word in text.split():
            valid = True
            for char in word:
                if char in brokenLetters:
                    valid = False
                    break
                    
            if valid:
                ret += 1
        return ret

