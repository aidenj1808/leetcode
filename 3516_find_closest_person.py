class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_to_z = abs(x - z)
        y_to_z = abs(y - z)
        if x_to_z == y_to_z:
            return 0
        elif x_to_z > y_to_z:
            return 2
        return 1

