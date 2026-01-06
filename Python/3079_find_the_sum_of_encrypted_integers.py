class Solution:
    def sumOfEncryptedInt(self, nums: list[int]) -> int:
        def encrypt(x):
            max_digit = 0
            x_string = str(x)
            for digit in x_string:
                max_digit = max(max_digit, int(digit))
            
            x_len = len(str(x_string))
            return int(f"{max_digit}" * x_len)

        return sum([encrypt(num) for num in nums])

