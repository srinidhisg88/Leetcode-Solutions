class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ## edge cases
        if dividend==divisor:
            return 1
        sign=True## both are positive
        if dividend<=0 and divisor>=0:
            sign=False
        if dividend>=0 and divisor<=0:
            sign=False
        n=abs(dividend)
        d=abs(divisor)
        ans=0
        while n>=d:
            cnt=0## 2^0
            while n>=(d<<(cnt+1)):
                cnt+=1
            ans+=(1<<cnt)
            n-=d*(1<<cnt)
        if ans>=2**31 and sign==True:
            return 2**31-1
        if ans>=2**31 and sign==False:
            return -2**31
        return ans if sign else -ans


        