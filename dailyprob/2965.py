class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        res=[0,0]
        num=[0]*(n*n+1)
        for i in range(n):
            for j in range(n):
                if num[grid[i][j]]==1:
                    res[0]=grid[i][j]
                else:
                    num[grid[i][j]]=1
        for i in range(1,n*n+1):
            if num[i]==0:
                res[1]=i
                break
        return res