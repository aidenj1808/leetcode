class Solution:
    # Optimize
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ret = []
        for i in range(len(nums1)):
            find_max = False
            for j in range(len(nums2)):
                if find_max and nums1[i] < nums2[j]:
                    ret.append(nums2[j])
                    break

                if nums1[i] == nums2[j]:
                    find_max = True

            if len(ret) != i + 1:
                ret.append(-1)
        return ret

