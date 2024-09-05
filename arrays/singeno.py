from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map=defaultdict(int)
        n=len(nums)
        for i in range(n):
            map[nums[i]]+=1
        for item,value in map.items():
            if value==1:
                return item
