class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        if len(grid) == 0:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count+=4
                    
                    if i > 0 and grid[i-1][j]: count-=1
                    if i < len(grid)-1 and grid[i+1][j]: count-=1
                    if j > 0 and grid[i][j-1]: count-=1
                    if j < len(grid[i])-1 and grid[i][j+1]: count-=1
        return count