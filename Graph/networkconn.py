class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ## count extra edges and find the p
        par=[i for i in range(n)]
        size=[1 for i in range(n)]
        def findPar(u):
            if  u==par[u]:
                return u
            up=findPar(par[u])
            par[u]=up
            return up
        def unionBysize(a,b):
            ulpu=findPar(a)
            ulpv=findPar(b)
            if ulpu==ulpv:return
            if size[ulpu]>size[ulpv]:
                par[ulpv]=ulpu
                size[ulpu]+=size[ulpv]
            else:
                par[ulpu]=ulpv
                size[ulpv]+=size[ulpu]
        cntextra=0
        for e in connections:
            u,v=e[0],e[1]
            if findPar(u)==findPar(v):
                cntextra+=1
            else:
                unionBysize(u,v)
        cntC=0
        for i in range(n):
            if par[i]==i:
                cntC+=1
        ans=cntC-1
        if cntextra>=ans:
            return ans
        return -1