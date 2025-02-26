class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum=0
        minsum=0
        for n in nums:
            maxsum=max(0,maxsum+n)
            minsum=min(0,minsum+n)
        return maxsum-minsum