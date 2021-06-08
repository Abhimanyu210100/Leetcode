class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        soln = []
        for i in range(1,numRows+1):
            temp = []
            for j in range(1,i+1):
                if i == 1:
                    temp.append(1)
                else:
                    if j == 1 or j == i:
                        temp.append(1)
                    else:
                        temp.append(soln[-1][j-2]+soln[-1][j-1])
            soln.append(temp)
        
        return soln