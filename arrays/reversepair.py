# here we have used merge sort solution
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ## using merge sort approach to get the 2 arrays
        return self.mergeSort(nums,0,len(nums)-1)
    def mergeSort(self,nums,si,ei):
        cnt=0
        if si>=ei:
            return cnt
        mid=(si+ei)//2
        cnt+=self.mergeSort(nums,si,mid)
        cnt+=self.mergeSort(nums,mid+1,ei)
        cnt+=self.cntpairs(nums,si,mid,ei)
        self.merge(nums,si,mid,ei)
        return cnt
    def merge(self,nums,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        while left<=mid and right<=high:
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1
            else:
                temp.append(nums[right])
                right+=1
        while left<=mid:
            temp.append(nums[left])
            left+=1
        while right<=high:
            temp.append(nums[right])
            right+=1
        for i in range(low,high+1):
            nums[i]=temp[i-low]
    
    def cntpairs(self,nums,low,mid,high):
        cnt=0
        right=mid+1
        for i in range(low,mid+1):
            while right<=high and nums[i]>2*nums[right]:
                right+=1
            cnt+=(right-(mid+1))
        return cnt
