class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letter = ord(coordinates[0]) - 96
        number = int(coordinates[1])
        if (letter + number) % 2 == 1:
            return True
        return False

