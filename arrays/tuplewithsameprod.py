class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prod_cnt=defaultdict(int)#n1*n2->count
        

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                
                prod_cnt[product]+=1
        res=0
        for cnt in prod_cnt.values():
            if cnt>1:

                pairs=(cnt*(cnt-1)//2)
                res+=8*pairs

        return res