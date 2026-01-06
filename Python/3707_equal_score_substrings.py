class Solution:
    def scoreBalance(self, s: str) -> bool:
        left_score = 0
        for i in range(len(s)):
            left_score += ord(s[i]) - 96

            right_score = 0
            for j in range(i + 1, len(s)):
                right_score += ord(s[j]) - 96
            
            if left_score == right_score:
                return True
        return False
        
