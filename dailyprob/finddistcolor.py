class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        f=Counter()
        res=[]
        color=defaultdict(int)
        for x,y in queries:
            prev=color[x]
            if prev!=0:
                f[prev]-=1
                if f[prev]==0:
                    del f[prev]
            color[x]=y
            f[y]+=1
            res.append(len(f))
        return res
