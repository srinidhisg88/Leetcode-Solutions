class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        cnt=0
        n=len(nums)
        res=set()
        for i in range(n):
            l=''
            cnt=0
            for j in range(i,n):
            
                
                if nums[j]%p==0:
                    cnt+=1
                l+=str(nums[j]) + ','
                if cnt>k:
                    break
                res.add(l)
               
        return len(res)