class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt=0
        n=len(A)
        seen=[0]*(n+1)
        ans=[]
        common=0
        for i in range(n):
            if seen[A[i]]==0:
                seen[A[i]]=1
            elif seen[A[i]]==1:
                common+=1
            if seen[B[i]]==0:
                seen[B[i]]=1
            elif seen[B[i]]==1:
                common+=1
            ans.append(common)

        
    
        return ans