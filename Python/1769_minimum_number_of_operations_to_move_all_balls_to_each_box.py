class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        ret_list = []
        operations = 0
        for i in range(len(boxes)):
            for j, trial_box in enumerate(boxes):
                if trial_box == "1":
                    operations += abs(i - j)
            ret_list.append(operations)
            operations = 0
        return ret_list

