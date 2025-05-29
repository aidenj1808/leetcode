class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        current_min = float("inf")
        ret = []
        for person_cost in cost:
            current_min = min(current_min, person_cost)
            ret.append(current_min)
        return ret

