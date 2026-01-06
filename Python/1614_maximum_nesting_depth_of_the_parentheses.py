class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxx = 0
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                stack.pop()
        
            maxx = max(maxx, len(stack))
        return maxx
            
