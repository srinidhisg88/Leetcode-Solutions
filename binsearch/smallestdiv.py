class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(mid):
            result=0
            for n in nums:
                result+=math.ceil(n/mid)
            return result<=threshold
        l,h=1,max(nums)
        ans=h
        while l<=h:
            mid=l+(h-l)//2
            if condition(mid):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans