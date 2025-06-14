class Solution:
    def minimumSum(self, num: int) -> int:
        digits_sorted = "".join(sorted(str(num)))
        ret = int(digits_sorted[0] + digits_sorted[2]) + int(digits_sorted[1] + digits_sorted[3])
        return ret

