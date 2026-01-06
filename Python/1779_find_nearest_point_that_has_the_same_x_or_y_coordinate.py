class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        min_distance = float("inf")
        min_i = -1
        for i in range(len(points)):
            a, b = points[i]
            if a != x and b != y:
                continue
            
            distance = abs(a - x) + abs(b - y)
            if distance < min_distance:
                min_distance = distance
                min_i = i

        return min_i

