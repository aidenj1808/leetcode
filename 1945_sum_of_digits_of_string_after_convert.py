class Solution:
    def getLucky(self, s: str, k: int) -> int:
        conversion = "".join([str(ord(char) - 96) for char in s])
        for _ in range(k):
            current_num = 0
            for digit in conversion:
                current_num += int(digit)
            conversion = str(current_num)
        return int(conversion)
        
