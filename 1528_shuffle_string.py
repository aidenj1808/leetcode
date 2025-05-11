import numpy


class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        ret = numpy.zeros(len(s), dtype=str)
        for char, i in zip(s, indices):
            ret[i] = char
        return "".join(ret)
        
