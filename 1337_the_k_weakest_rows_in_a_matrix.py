class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        mat_sorted = sorted(enumerate(mat), key=lambda x: (sum(x[1]), x[0]))
        return [i for i, _ in mat_sorted][: k]

