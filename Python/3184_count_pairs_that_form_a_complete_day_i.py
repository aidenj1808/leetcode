class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        ret = 0
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    ret += 1
        return ret
        
