class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        days=0
        q=deque([])
        totcnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]!=0:
                    totcnt+=1
        
        dx=(0,-1,0,+1)
        dy=(-1,0,+1,0)
        cnt=0
        while  q:
          
            t=len(q)
            cnt+=t
            for _ in range(t):
                x,y=q.popleft()
                for i in range(0,4):
                    nx=x+dx[i]
                    ny=y+dy[i]
                    if(nx<0 or ny<0 or nx>=m or ny>=n or grid[nx][ny]!=1):
                        continue
                    grid[nx][ny]=2
                    q.append((nx,ny))
            if q:
                days+=1
        return days if totcnt==cnt else -1