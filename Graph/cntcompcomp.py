class UnionFind:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n
    def find(self,a):
        if a!=self.parent[a]:
            self.parent[a]=self.find(self.parent[a])
        return self.parent[a]
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b:
            return False
        else:
            if self.size[a]<self.size[b]:
                self.parent[a]=self.parent[b]
                self.size[b]+=self.size[a]
            else:
                self.parent[b]=self.parent[a]
                self.size[a]+=self.size[b]
        return False

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # count no of components
        uf=UnionFind(n)
        cnt=0
        for a,b in edges:
            uf.union(a,b)
           
        comp_size=[0]*n
        comp_edges=[0]*n
        for i in range(n):
            comp_size[uf.find(i)]+=1
        
        for u,v in edges:
            comp_edges[uf.find(u)]+=1
        
        count=0
        for i in range(n):
            if uf.find(i)==i:
                if comp_edges[i]==comp_size[i]*(comp_size[i]-1)//2:
                    count+=1
        return count
        
