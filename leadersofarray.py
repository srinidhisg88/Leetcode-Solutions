class Solution:
    def leader(self,nums):
        newl=[]
        max=float('-inf')
        for i in range(len(nums)-1,0,-1):
            if nums[i]>max:
                newl.append(nums[i])
                max=nums[i]
        return newl
soln=Solution()
arr=[10,22,2,0,6]
print(soln.leader(arr))