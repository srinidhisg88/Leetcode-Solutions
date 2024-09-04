class Solution(object):
    def cntgoodno(self,n:int)->int:
        a=(n+1)/2
        b=n/2
        mod=10**9+7
        return pow(5,a,mod)*pow(5,b,mod)%mod