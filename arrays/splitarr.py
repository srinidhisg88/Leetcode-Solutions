class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ## prefix
        n=len(nums)
        prefix=[0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i]=nums[i]+prefix[i-1]
        cnt=sum(1 for i in range(n-1) if prefix[i]>=prefix[-1]-prefix[i])
        return cnt