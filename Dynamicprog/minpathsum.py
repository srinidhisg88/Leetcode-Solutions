class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ## dynamic programming top down approach
        ## along 1st row and 1st column we there is no need to compare
        cache=[[float('inf')]*(len(grid[0])) for i in range(len(grid))]
        minsum=0
        
        for i in range(len(grid)):
            minsum+=grid[i][0]
            cache[i][0]=minsum
        minsum=0
        for i in range(len(grid[0])):
            minsum+=grid[0][i]
            cache[0][i]=minsum
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                
                cache[i][j]=min(cache[i-1][j],cache[i][j-1])+grid[i][j]
        return cache[len(grid)-1][len(grid[0])-1]