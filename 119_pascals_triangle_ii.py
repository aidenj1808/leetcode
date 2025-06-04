class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        
        current_row = [1, 1]
        new_row = []
        for _ in range(rowIndex - 1):
            new_row.append(current_row[0])
            for i in range(1, len(current_row)):
                new_row.append(current_row[i] + current_row[i - 1])
            new_row.append(current_row[-1])
            current_row = new_row
            new_row = []
        return current_row

