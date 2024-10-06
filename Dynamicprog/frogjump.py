class Solution:
    ## using memoization
    def frogJump(self,i,dp:list[int],heights:list[int]):
        if i==0:
            return 0
        left=self.frogJump(i-1,dp)+abs(height[i]-height[i-1])
        if i>1:
            right=self.frogJump(i-2,dp)+abs(height[i]-height[i-2])
        return dp[i]= min(left,right)
    ## using tabulation
    dp[0]=0
    for i in range(1,n):
        