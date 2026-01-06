class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        ans1 = set()
        ans2 = set()
        for num in nums1:
            if num not in nums2_set:
                ans1.add(num)
        
        for num in nums2:
            if num not in nums1_set:
                ans2.add(num)
        return [list(ans1), list(ans2)]

