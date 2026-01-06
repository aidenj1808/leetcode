class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        ans1 = 0
        ans2 = 0
        for num in nums1:
            if num in nums2_set:
                ans1 += 1
        
        for num in nums2:
            if num in nums1_set:
                ans2 += 1
        return [ans1, ans2]

