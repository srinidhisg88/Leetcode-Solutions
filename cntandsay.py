class Solution:
    def countAndSay(self, n: int) -> str:
        def helper(ans:str):
            cnt=1
            result=''
            for i in range(len(ans)):
                if i==len(ans)-1 or ans[i]!=ans[i+1]:
                    result+=str(cnt)+ans[i]
                    cnt=1
                else:
                    cnt+=1
            return result
        ans='1'
        for i in range(2,n+1):
            ans=helper(ans)
        return ans