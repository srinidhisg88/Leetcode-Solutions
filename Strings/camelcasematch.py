class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(query,pattern):
            i=0
            cap=0
            for j in range(0,len(query)):
                if i<len(pattern) and pattern[i]==query[j]:
                    i+=1
                elif query[j]>='A' and query[j]<='Z':
                    cap+=1
            return (i==len(pattern) and cap==0)
        ans=[]
        for i in range(len(queries)):
            ch=check(queries[i],pattern)
            ans.append(ch)
        return ans