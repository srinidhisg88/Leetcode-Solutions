class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
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
        hashmap={}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail=accounts[i][j]
                if mail not in hashmap:
                    hashmap[mail]=i
                else:
                    unionBysize(i,hashmap[mail])
        mergedmail=[[] for _ in range(n)]
        for mail,node in hashmap.items():
            mergedmail[findPar(node)].append(mail)
        ans=[]
        for i in range(n):
            if mergedmail[i]:
                mergedmail[i].sort()
                ans.append([accounts[i][0]]+mergedmail[i])
        return ans
