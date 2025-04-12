class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<m*k:
            return -1
        def canMakeBouquets(mid):
            b=f=0
            for d in bloomDay:
                if d<=mid:
                    f+=1
                    if f==k:
                        b+=1
                        f=0
                else:
                    f=0
            return b>=m
        low=1
        high=max(bloomDay)
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            
            if canMakeBouquets(mid):
                ans=mid
                high=mid-1
                
            else:
                low=mid+1
        return ans
