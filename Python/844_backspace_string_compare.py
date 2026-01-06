class Solution:
    # TC O(n) SC O(n), Optimize for SC O(1) using two pointers
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        for s_char in s:
            if s_char != "#":
                s_stack.append(s_char)
            elif len(s_stack) != 0:
                s_stack.pop()
        
        t_stack = []
        for t_char in t:
            if t_char != "#":
                t_stack.append(t_char)
            elif len(t_stack) != 0:
                t_stack.pop()
        
        return s_stack == t_stack

