class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0
        for char in s:
            if char == 'L':
                balance += 1
            else:
                balance -= 1
            
            if not balance:
                ans += 1
        return ans
        
