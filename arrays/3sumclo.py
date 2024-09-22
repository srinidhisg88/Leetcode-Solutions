class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ## binarysearch
        nums.sort()
        n=len(nums)
        cnt=0
        res=sum(nums[:3])
        for i in range(n-2):
            
            l=i+1
            r=n-1
            while l<r:
                su=nums[i]+nums[l]+nums[r]
                if abs(su-target)<abs(res-target):
                    res=su
                if su<target:
                    l+=1
                else:
                    r-=1
                
        return res
                