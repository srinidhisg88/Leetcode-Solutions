class Solution:
    def myAtoi(self, s: str) -> int:
        ans=0
        
        i=0
        sign=1
        n=len(s)
        if n==0:
            return 0
        while i<n and s[i]==' ':
            i+=1
        if i==n:
            return 0
        ## check for sign
        if i<n and (s[i]=='-' or s[i]=='+'):
            sign=-1 if s[i]=='-' else 1
            i+=1
        ## convert digits into integer
        while i<n and s[i].isdigit():
            ans=ans*10+int(s[i])
            if ans*sign<=-2**31:
                return -2**31
            if ans*sign>=2**31-1:
                return 2**31-1
            i+=1
        return ans*sign
