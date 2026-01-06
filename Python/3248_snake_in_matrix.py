class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        current_position = [0, 0]
        for command in commands:
            match command:
                case "LEFT":
                    current_position[1] = current_position[1] - 1
                case "RIGHT":
                    current_position[1] = current_position[1] + 1
                case "UP":
                    current_position[0] = current_position[0] - 1
                case "DOWN":
                    current_position[0] = current_position[0] + 1
        return (current_position[0] * n) + current_position[1]
        
