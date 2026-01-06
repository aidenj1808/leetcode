class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        p1 = 0
        p2 = 2
        while p2 < len(arr):
            valid = True
            for num in arr[p1: p2 + 1]:
                if num % 2 == 0:
                    valid = False
            
            if valid:
                return True

            p1 += 1
            p2 += 1

        return False

