class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.subarray(nums,goal)-self.subarray(nums,goal-1)
    def subarray(self,nums,goal):
        if goal<0:
            return 0
        l=0
        r=0
        sum=0
        cnt=0
        n=len(nums)
        while r<n:
            sum+=nums[r]
            while sum>goal:
                sum-=nums[l]
                l+=1
            cnt+=(r-l+1)
            r+=1
        return cnt