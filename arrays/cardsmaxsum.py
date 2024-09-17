class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        lsum=0
        rsum=0
        for i in range(0,k):
            lsum+=nums[i]
        maxsum=lsum
        ridx=len(nums)-1
        for i in range(k-1,-1,-1):
            lsum-=nums[i]
            rsum+=nums[ridx]
            ridx-=1
            maxsum=max(maxsum,lsum+rsum)
        return maxsum