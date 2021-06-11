class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum1 = 0
        for i in range(len(mat)):
            sum1+=mat[0+i][0+i] + mat[0+i][len(mat)-1-i]
        if len(mat)%2==0: return sum1
        if len(mat)%2==1:
            sum1-=mat[int(floor(len(mat)/2))][int(floor(len(mat)/2))]
            return sum1
        