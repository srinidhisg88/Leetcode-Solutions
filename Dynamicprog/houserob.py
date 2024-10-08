class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        ## use tabulation process
        dp[0]=nums[0]
        neg=0
        for i in range(1,len(nums),1):
            take=nums[i]
            if i>1:
                take+=dp[i-2]
            notake=dp[i-1]
            dp[i]=max(take,notake)
        return dp[len(nums)-1]