class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        ans = []
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        nums3_set = set(nums3)
        for number in nums1_set:
            if number in nums2_set or number in nums3_set:
                ans.append(number)

        for number in nums2_set:
            if number in nums1_set or number in nums3_set:
                ans.append(number)

        for number in nums3_set:
            if number in nums1_set or number in nums2_set:
                ans.append(number)

        return list(set(ans))
