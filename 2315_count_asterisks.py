class Solution:
    def countAsterisks(self, s: str) -> int:
        in_bar = 0
        ret = 0
        for char in s:
            if char == "|" and in_bar:
                in_bar -= 1
            elif char == "|":
                in_bar += 1
            
            if char == "*" and not in_bar:
                ret += 1
        return ret
        
