class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        ret_list = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                ret_list.append(i)
        return ret_list

