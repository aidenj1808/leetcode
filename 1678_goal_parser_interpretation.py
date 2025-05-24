class Solution:
    def interpret(self, command: str) -> str:
        ret = ""
        for i in range(len(command)):
            if command[i] == "G":
                ret += "G"
            elif command[i: i + 2] == "()":
                ret += "o"
            elif command[i: i + 2] == "(a":
                ret += "al"
        return ret

