class Solution:
    def nextPermutation(self,nums):
        # find the break point where there is a sudden dip
        ind=-1
        for i in range(len(nums)-2,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            nums.reverse()
            return nums
        #find a number which closely greater than nums[i]
        for i in range(len(nums)-2,ind-1):
            if(nums[i]>nums[ind]):
                temp=nums[ind]
                nums[ind]=nums[i]
                nums[i]=temp
                break
        #sort the remaining part after break point to get the lowest arrangement
        nums[ind+1:]=reversed(nums[ind+1:])
        return nums
soln=Solution()
arr=[3,2,1]
print(soln.nextPermutation(arr))