class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        max_val=float('inf')
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<=0:
                l=mid+1
            else:
                r=mid-1
        pos=len(nums)-l
        l-=1
        while l>=0 and nums[l]==0:
            l-=1
        neg=l+1
        return max(pos,neg)