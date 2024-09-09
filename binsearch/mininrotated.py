class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        ans=sys.maxsize
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if nums[low]<=nums[high]:## whole space is already sorted
                ans=min(nums[low],ans)
                break
            if nums[low]<=nums[mid]:## if left part is sorted
                ans=min(nums[low],ans)
                low=mid+1
            else:
                ans=min(nums[mid],ans)
                high=mid-1
        return ans

    
        