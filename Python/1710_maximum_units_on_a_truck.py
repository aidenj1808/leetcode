class Solution:
    # Optimize
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxes_sorted = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        ret = 0
        boxes_taken = 0

        i = 0
        while boxes_taken < truckSize and i < len(boxes_sorted):
            num, units = boxes_sorted[i]
            i += 1

            j = 0
            while boxes_taken < truckSize and j < num:
                ret += units
                boxes_taken += 1
                j += 1                      
        return ret

