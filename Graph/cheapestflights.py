
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ## dijstra's algorithm based on the fact that we add to the priority queue based on less no of stops
        q=deque([(0,src,0)])
        ##m queue will be in the form (stops,node,dist from source)
        dist=[float('inf') for _ in range(n)]
        
        dist[src]=0
        m=len(flights)
        adj=defaultdict(list)

        for i in range(m):
            adj[flights[i][0]].append((flights[i][1],flights[i][2]))
        while q:
            stops,node,cost=q.popleft()
            if stops>k:
                continue
            for n in adj[node]:
                if dist[n[0]]>cost+n[1] and stops<=k:
                    dist[n[0]]=cost+n[1]
                    q.append((stops+1,n[0],cost+n[1]))
        if dist[dst]!=float('inf'):
            return dist[dst]
        return -1
