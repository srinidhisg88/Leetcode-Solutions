class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map=defaultdict(int)
        n=len(nums)
        i=0
        newl=[]
        for i in range(n):
            map[nums[i]]+=1
        for item,value in map.items():
            if value>n/3:
                newl.append(item)
        return newl
        