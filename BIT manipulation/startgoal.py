class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # use XOR to get the count
        # number of 1 bits in the result gives the final answer
        cnt=0
        res=start^goal
        while res>0:
            if res&1==1:
                cnt+=1
            res=res>>1# tc is O(logn)
        return cnt