class Solution:
    def findGCD(self, nums: list[int]) -> int:
        minn = float("inf")
        maxx = float("-inf")
        for i in range(len(nums)):
            if nums[i] < minn:
                minn = nums[i]
            
            if nums[i] > maxx:
                maxx = nums[i]
        
        gcd = 0
        for x in range(1, minn + 1):
            if minn % x == 0 and maxx % x == 0:
                gcd = x
        return gcd
 
