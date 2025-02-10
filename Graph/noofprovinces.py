class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ## this is same as dfs of graph
        n=len(isConnected)
        visited=[False]*n
        dfscnt=0
        cnt=[0]
        def dfs(v):
            cnt[0]+=1
            if visited[v]:
                return
            
            visited[v]=True
            for i in range(n):
                if not visited[i] and isConnected[v][i]==1:
                    dfs(i)
        dfs(0)
        dfscnt+=1
        if cnt[0]<=n:
            for i in range(n):
                if not visited[i]:
                    dfs(i)
                    dfscnt+=1
        return dfscnt