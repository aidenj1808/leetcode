class Solution:
    def minimumFlips(self, n: int) -> int:
        bin_string = f"{n:b}"
        reverse_bin_string = bin_string[::-1]
        flips = 0
        for i in range(len(bin_string)):
            if bin_string[i] != reverse_bin_string[i]:
                flips += 1
        return flips
        
