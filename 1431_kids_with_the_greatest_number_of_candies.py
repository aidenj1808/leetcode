class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        ret_list = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                ret_list.append(True)
            else:
                ret_list.append(False)
        return ret_list

