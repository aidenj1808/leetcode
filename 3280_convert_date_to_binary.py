class Solution:
    def convertDateToBinary(self, date: str) -> str:
        decimal_string_list = [num for num in date.split("-")]
        binary_string_list = []
        for num in decimal_string_list:
            binary_string_list.append(bin(int(num))[2:])
        return "-".join(binary_string_list)

