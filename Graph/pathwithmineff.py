from queue import PriorityQueue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        q=PriorityQueue()
        R=len(heights)
        C=len(heights[0])
        q.put((0,0,0))
        dist=[[float('inf')]*C for _ in range(R)]
        dir=((1,0),(-1,0),(0,1),(0,-1))
        while not q.empty():
            diff,x,y=q.get()
            if x==R-1 and y==C-1:
                return diff
            for dx,dy in dir:
                nr=x+dx
                nc=y+dy
                if nr>=0 and nc>=0 and nr<R and nc<C:
                    neweff=max(abs(heights[x][y]-heights[nr][nc]),diff)
                    if neweff<dist[nr][nc]:
                        dist[nr][nc]=neweff
                        q.put((neweff,nr,nc))
        return 0
            