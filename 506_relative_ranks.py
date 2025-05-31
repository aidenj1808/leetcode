class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        score_indices = {score[i]: i for i in range(len(score))}
        score_sorted = sorted(score, reverse=True)
        ret = ['0'] * len(score)
        for i, s in enumerate(score_sorted):
            match i:
                case 0:
                    ret[score_indices[s]] = "Gold Medal"
                case 1:
                    ret[score_indices[s]] = "Silver Medal"
                case 2:
                    ret[score_indices[s]] = "Bronze Medal"
                case _:
                    ret[score_indices[s]] = str(i + 1)
        return ret

