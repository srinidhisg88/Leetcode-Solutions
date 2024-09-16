class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ## using two pointer and sliding windowe approach
        l=0
        r=0
        maxlen=0
        zeroes=0
        while r<len(nums):
            if nums[r]==0:
                zeroes+=1
            if zeroes>k:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            if zeroes<=k:## we are not updating the maxlength untill we trim down the zeroes <=k
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
                
            