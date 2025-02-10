class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q=deque([])
        startval=image[sr][sc]
        R=len(image)
        C=len(image[0])
        if startval==color:
            return image
        q.append((sr,sc))

        dx=(0,-1,0,+1)
        dy=(-1,0,+1,0)
        while q:
            n=len(q)
            for _ in range(n):
                r,c=q.popleft()
                image[r][c]=color
                for i in range(4):
                    nx=r+dx[i]
                    ny=c+dy[i]
                    if nx<0 or ny<0 or nx>=R or ny>=C or image[nx][ny]!=startval:
                        continue
                    
                    q.append((nx,ny))
        return image