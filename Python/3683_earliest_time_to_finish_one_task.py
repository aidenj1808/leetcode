class Solution:
    def earliestTime(self, tasks: list[list[int]]) -> int:
        min_time = float("inf")
        for start_task, end_task in tasks:
            min_time = min(start_task + end_task, min_time)
        return min_time

