class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def permutation(i,nums,ans):
            if i==len(nums):
                ans.append(nums[:])
            for ind in range(i,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                permutation(i+1,nums,ans)
                nums[ind],nums[i]=nums[i],nums[ind]
        permutation(0,nums,ans)
        return ans