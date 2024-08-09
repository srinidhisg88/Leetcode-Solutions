class Solution(object):
    def missingno(self,nums):
        n=len(nums)
        xor1=0
        for i in range(1,n+1,1):
            xor1^=i
        xor2=0
        for i in nums:
            xor2^=i
        return xor1^xor2
soln=Solution()
print(soln.missingno([0,2,3]))