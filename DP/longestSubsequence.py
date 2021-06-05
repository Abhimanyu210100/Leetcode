class Solution:
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        soln = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    soln[i][j]=soln[i-1][j-1]+1
                else:
                    soln[i][j]=max(soln[i-1][j],soln[i][j-1])
        return soln[m][n]
        
    
    
            
        