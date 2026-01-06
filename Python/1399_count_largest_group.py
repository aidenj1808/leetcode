from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sums = {}
        for x in range(1, n + 1):
            cur_sum = 0
            for digit in str(x):
                cur_sum += int(digit)
            digit_sums[x] = cur_sum

        c = Counter(digit_sums.values())
        values_count = c.most_common()
        most_common_value = values_count[0][1]
        return len([value for _, value in values_count if value == most_common_value])
        
