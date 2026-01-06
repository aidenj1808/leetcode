class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        ret = []
        for row in image:
            row = [0 if num == 1 else 1 for num in row][::-1]
            print(row)
            ret.append(row)
        return ret
        
