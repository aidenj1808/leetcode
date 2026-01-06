class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        ret = 0
        n = len(mat)
        for i in range(n):
            ret += mat[i][i]
            ret += mat[i][n - i - 1]

        if n % 2 != 0:
            return ret - mat[n // 2][n // 2]
        return ret
        
