class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        for num1 in set(aliceSizes):
            #Rewriting the formula from below
            if (num1 + (sumBob - sumAlice)/2) in set(bobSizes):
                return [num1, int(num1 + (sumBob - sumAlice)/2)]
            
#             for num2 in set(bobSizes):
#                 sumAlice_new = sumAlice + num2 - num1
#                 sumBob_new = sumBob + num1 - num2
#                 if sumAlice_new == sumBob_new:
#                     return [num1,num2]
        