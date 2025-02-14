class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R=len(grid)
        C=len(grid[0])
        visited=[[0]*C for _ in range(R)]
        def bfs(i,j):
            q=deque([(i,j)])
            visited[i][j]=1
            while q:
                r,c=q.popleft()
                
                directions=[(-1,0),(1,0),(0,-1),(0,1)]
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr>=0 and nc>=0 and nr<R and nc<C and grid[nr][nc]=='1' and visited[nr][nc]==0:
                        visited[nr][nc]=1
                        q.append((nr,nc))


            
        cnt=0
        for i in range(R):
            for j in range(C):
                if visited[i][j]==0 and grid[i][j]=='1':
                    cnt+=1
                    bfs(i,j)
        return cnt