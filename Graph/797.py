class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        
        path=[]
        ans=[]
        def dfs(i):
            
            path.append(i)
            if i==len(graph)-1:
                
                ans.append(path[:])
            
            for n in graph[i]:
                
                dfs(n)
            path.pop()
        dfs(0)
        return ans