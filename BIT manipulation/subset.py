class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resl=[]
        n=len(nums)
        subset=1<<n# which mean 2^n
        for num in range(0,subset):
            temp=[]
            for i in range(0,n):
                if num&(1<<i):
                    temp.append(nums[i])
            resl.append(temp)
        return resl

                