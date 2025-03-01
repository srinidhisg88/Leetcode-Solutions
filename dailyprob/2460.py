class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros=[]
        n=len(nums)
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
                zeros.append(0)
            else:
                continue
        newnums=[num for num in nums if num!=0]
        
        newnums.extend([0]*(n-len(newnums)))
        return newnums
        ##print(nums)