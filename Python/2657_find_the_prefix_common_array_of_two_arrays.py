class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        a_seen = set()
        b_seen = set()
        c = []
        for i in range(len(A)):
            a_seen.add(A[i])
            b_seen.add(B[i])
            c.append(len(a_seen & b_seen))
        return c
        
