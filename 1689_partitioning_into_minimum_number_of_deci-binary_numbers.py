class Solution:
    def minPartitions(self, n: str) -> int:
        ret = "0"
        for char in n:
            if char > ret:
                ret = char
        return int(ret)
        
