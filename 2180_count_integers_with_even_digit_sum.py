class Solution:
    def countEven(self, num: int) -> int:
        ret = 0
        nums = [str(x) for x in range(1, num + 1)]
        for x in nums:
            total = 0
            for digit in x:
                total += int(digit)
            
            if total % 2 == 0:
                ret += 1
        return ret

