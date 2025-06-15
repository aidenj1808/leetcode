class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = str(num)[::-1]
        reversed2 = str(int(reversed1))[::-1]
        return num == int(reversed2)
        
