from typing import List
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)

        rank_score ={}

        for i, s in enumerate(sorted_score):
            if i == 0:
                rank_score[s] = "Gold Medal"
            elif i == 1:
                rank_score[s] = "Silver Medal"
            elif i == 2:
                rank_score[s] = "Bronze Medal"
            else:
                rank_score[s] = str(i + 1)
        return [rank_score[s] for s in score]