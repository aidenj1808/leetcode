from collections import Counter

class Solution:
    def checkPrimeFrequency(self, nums: list[int]) -> bool:
        c = Counter(nums)
        ret = False
        for _, count in c.items():
            if count == 1:
                continue
                
            is_prime = True
            for x in range(2, count):
                if count % x == 0:
                    is_prime = False
            
            if is_prime:
                return True
        return ret
        
