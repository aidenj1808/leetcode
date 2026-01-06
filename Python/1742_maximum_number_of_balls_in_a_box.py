class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes_counts = {}
        for x in range(lowLimit, highLimit + 1):
            cur_sum = 0
            for digit in str(x):
                cur_sum += int(digit)
            
            if cur_sum not in boxes_counts:
                boxes_counts[cur_sum] = 0
            boxes_counts[cur_sum] += 1
        
        return max(boxes_counts.values())

