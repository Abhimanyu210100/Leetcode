class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # if tops.count(tops[0]) + bottoms.count(tops[0]) < len(tops):
        #     return -1
        # if tops.count(tops[0]) + bottoms.count(tops[0]) < len(tops) and tops.count(bottoms[0]) + bottoms.count(bottoms[0]) < len(tops):
        #     return -1
        # if tops.count(bottoms[0]) + bottoms.count(bottoms[0]) < len(bottoms):
        #     print('hey')
        #     return -1
        count_top=0
        count_bot=0
        soln1=0
        for i in range(len(tops)):
            if tops[i] != tops[0] and bottoms[i]!= tops[0]:
                soln1 = -1
                break
            else:
                if tops[i]!= tops[0]: count_top+=1
                if bottoms[i]!= tops[0]: count_bot+=1
        if soln1 != -1: soln1 = min(count_top,count_bot)
        
        count_top=0
        count_bot=0
        soln2=0
        for i in range(len(bottoms)):
            if bottoms[i]!=bottoms[0] and tops[i]!=bottoms[0]:
                soln2 = -1
                break
            else:
                if tops[i]!=bottoms[0]:count_top+=1
                if bottoms[i]!=bottoms[0]:count_bot+=1
        if soln2!=-1: soln2 = min(count_top,count_bot)
        if min(soln1,soln2)>0: return min(soln1,soln2)
        else: return max(soln1,soln2)