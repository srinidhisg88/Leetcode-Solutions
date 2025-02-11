class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=[False]*len(graph)
        color=[False]*(len(graph))
        n=len(graph)
        def dfs(u):
            for v in graph[u]:
                if not visited[v]:
                    visited[v]=True
                    color[v]=not color[u]
                    if not dfs(v):
                        return False
                elif color[v]==color[u]:
                    return False
            return True

        for i in range(n):
            if not visited[i]:
                visited[i]=True
                color[i]=True
                if not dfs(i):
                    return False
        return True
        