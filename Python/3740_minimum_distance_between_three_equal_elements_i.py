class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        min_distance = float("inf")
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] == nums[j] == nums[k]:
                        distance = abs(i - j) + abs(j - k) + abs(k - i)
                        min_distance = min(min_distance, distance)
                        print(min_distance)
        return min_distance if min_distance != float("inf") else -1
        
