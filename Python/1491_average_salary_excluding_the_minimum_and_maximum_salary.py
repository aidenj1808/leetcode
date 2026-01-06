class Solution:
    def average(self, salary: list[int]) -> float:
        return sum(sorted(salary)[1: -1]) / (len(salary) - 2)
        
