class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        row_sums = [sum(row) for row in mat] 
        col_sums = []
        for i in range(cols):
            current_sum = 0
            for j in range(rows):
                current_sum += mat[j][i]
            col_sums.append(current_sum)

        ret = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_sums[i] == 1 and col_sums[j] == 1:
                    ret += 1
        return ret

