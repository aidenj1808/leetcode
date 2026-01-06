class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        deletions = 0
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[j - 1][i] > strs[j][i]:
                    deletions += 1
                    break
        return deletions

