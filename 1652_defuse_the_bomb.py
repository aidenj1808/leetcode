class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        ret = [0 for _ in range(len(code))]
        n = len(code)
        if k == 0:
            return ret
        elif k > 0:
            for i in range(len(code)):
                ret[i] = sum([code[j % n] for j in range(i + 1, i + 1 + k)])
        else:
            for i in range(len(code)):
                ret[i] = sum([code[j % n] for j in range(i + k, i)])
        return ret
        
