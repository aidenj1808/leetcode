class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        ret = []
        for value1 in [-1 * t, 1 * t]:
            for value2 in [-1 * t, 1 * t]:
                y = num + value1
                x = y + value2 * -1
                ret.append(x)
        return max(ret)
            
