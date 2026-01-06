class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left_of_pivot = []
        pivots = []
        right_of_pivot = []
        for num in nums:
            if num == pivot:
                pivots.append(num)
            elif num < pivot:
                left_of_pivot.append(num)
            else:
                right_of_pivot.append(num)
        return left_of_pivot + pivots + right_of_pivot
        
