class Solution:
    def decimalRepresentation(self, n: int) -> list[int]:
        multiplier = 1
        ret = []
        for i in range(len(str(n)) - 1, -1, -1):
            component = int(str(n)[i]) * multiplier
            if component:
                ret.append(component)
            multiplier *= 10
        return ret[::-1]

