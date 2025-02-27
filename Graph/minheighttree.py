class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        # initialize the adjacency list and degree of each node
        adj=defaultdict(list)
        degree=[0]*n
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1
        leaves=deque([i for i in range(n) if degree[i]==1])

        rem_nodes=n
        while rem_nodes>2:
            leav_cnt=len(leaves)
            rem_nodes-=leav_cnt
            for _ in range(leav_cnt):
                leaf=leaves.popleft()
                for n in adj[leaf]:
                    degree[n]-=1
                    if degree[n]==1:
                        leaves.append(n)
        return list(leaves)