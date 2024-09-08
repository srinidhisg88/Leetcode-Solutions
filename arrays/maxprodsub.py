class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        ## using 2 pointer approach
        # maxprod=nums[0]
        # prod=1
        # n=len(nums)
        
        # for i in range(n-1):
        #     prod=nums[i]
        #     for j in range(i+1,n):
        #         maxprod=max(maxprod,prod)
        #         prod*=nums[j]
                
        #     maxprod=max(prod,maxprod)
            
        # return maxprod
        ## do not use kadanes on this problem as it is not intuitive
        ## using prefix and suffix method
        prefix=1
        suffix=1
        ans=float('-inf')
        n=len(nums)
        for i in range(n):
            if prefix==0:
                prefix=1
            if suffix==0:
                suffix=1
            prefix*=nums[i]
            suffix*=nums[n-1-i]
            ans=max(ans,max(prefix,suffix))
        return ans

        