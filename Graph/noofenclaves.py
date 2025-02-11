class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ## traverse all the  1 from boundaries and increase the count for unvisited lands
        q=deque([])
        R=len(grid)
        C=len(grid[0])
        visited=[[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if (i==0 or j==0 or i==R-1 or j==C-1) and grid[i][j]==1:
                    q.append((i,j))
                    visited[i][j]=1
        dx=(+1,0,-1,0)
        dy=(0,+1,0,-1)
        while q:
            x,y=q.popleft()
            
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and ny>=0 and nx<R and ny<C and grid[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny))
        cnt=0
        for i in range(R):
            for j in range(C):
                if visited[i][j]==0 and grid[i][j]==1:
                    cnt+=1
        return cnt