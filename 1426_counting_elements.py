class Solution:
    def countElements(self, arr: list[int]) -> int:
        arr_set = set(arr)
        ret = 0
        for x in arr:
            if x + 1 in arr_set:
                ret += 1
        return ret


s = Solution()
print(s.countElements([1, 2, 3]), "should be 2")
print(s.countElements([1, 1, 3, 3, 5, 5, 7, 7]), "should be 0")
print(s.countElements([1, 3, 2, 3, 5, 0]), "should be 3")

