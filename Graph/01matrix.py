class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #same as rotten oranges
        q=deque([])
        R,C=len(mat),len(mat[0])
        visited=[[0]*C for _ in range(R)]
        dist=[[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    visited[i][j]=1
                else:
                    visited[i][j]=0
        
        dx=(0,-1,0,+1)
        dy=(-1,0,+1,0)
        #multisource dfs
        while q:
            x,y,d=q.popleft()
            dist[x][y]=d
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if nx>=0 and ny>=0 and nx<R and ny<C and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    q.append((nx,ny,d+1))

        return dist

