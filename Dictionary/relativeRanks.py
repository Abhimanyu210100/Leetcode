class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        rankings = {}
        for i in range(len(sorted_score)):
            if i == 0: rankings[sorted_score[i]] = 'Gold Medal'
            elif i == 1: rankings[sorted_score[i]] = 'Silver Medal'
            elif i == 2: rankings[sorted_score[i]] = 'Bronze Medal'
            else: rankings[sorted_score[i]] = str(i+1)
        return [rankings[points] for points in score]
        
        