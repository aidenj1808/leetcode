class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        # Optimize with two pointers
        def populate_dictionary(nums: list[list[int]], my_dict: dict[int, int]):
            for nums_id, val in nums:
                if nums_id not in my_dict:
                    my_dict[nums_id] = 0
                my_dict[nums_id] += val
        
        counts = {}
        populate_dictionary(nums1, counts)
        populate_dictionary(nums2, counts)

        return [[nums_id, val] for nums_id, val in sorted(counts.items(), key=lambda x: x[0])]
        
