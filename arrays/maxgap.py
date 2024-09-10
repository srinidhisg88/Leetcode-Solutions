from collections import defaultdict
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        if n<2:
            return 0
        if n==2:
            return abs(nums[0]-nums[1])
        hashmap=defaultdict(int)
        maxdiff=float('-inf')
        for i in range(n-1):
            hashmap[i]=abs(nums[i]-nums[i+1])
            maxdiff=max(hashmap[i],maxdiff)
        return int(maxdiff)
