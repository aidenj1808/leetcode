class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[i - 1] + self.nums[i])


    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] + self.nums[left] - self.prefix_sum[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
