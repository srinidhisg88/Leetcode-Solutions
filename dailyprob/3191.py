from collections import defaultdict
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ## fixed window solution
        ## use of xor
        n=len(nums)
        k=0
        for i in range(n-2):
            if nums[i]==0:
                nums[i]^=1
                nums[i+1]^=1
                nums[i+2]^=1
                k+=1
        return -1 if 0 in nums else k