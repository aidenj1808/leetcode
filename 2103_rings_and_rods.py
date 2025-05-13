class Solution:
    def countPoints(self, rings: str) -> int:
        rod_rings_counts = {}
        for i in range(1, len(rings), 2):
            rod = rings[i]
            ring_colour = rings[i - 1]
            if rod not in rod_rings_counts:
                rod_rings_counts[rod] = set()
            rod_rings_counts[rod].add(ring_colour)
        
        ret = 0
        for _, count in rod_rings_counts.items():
            if len(count) == 3:
                ret += 1
        return ret
        
