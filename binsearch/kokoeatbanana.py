class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ## banana eating per hr can be upto max of piles
        
        max_val=max(piles)
        left=1
        right=max_val
        ans=right
        while left<=right:
            mid=(left+right)//2
            hrs_needed=sum(math.ceil(pile/mid) for pile in piles)
            if hrs_needed<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
            

