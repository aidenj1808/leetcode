class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        cell_range = s.split(':')

        cols_range = cell_range[0][0] + cell_range[1][0]
        cols_range = [chr(65 + i) for i in range(ord(cols_range[0]) - 65, ord(cols_range[1]) - 64)]

        rows_range = cell_range[0][1] + cell_range[1][1]
        rows_range = [i for i in range(int(rows_range[0]), int(rows_range[1]) + 1)]

        ret = []
        for col in cols_range:
            for row in rows_range:
                ret.append(col + str(row))
        return ret

