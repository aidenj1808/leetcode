class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        ret = arrivalTime + delayedTime
        return ret % 24
        
