class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        hashmap=defaultdict(list)
        newl=[]
        n=len(nums)
        for i in range(n):
            if nums[i]%2==0:
                hashmap[0].append(nums[i])
            else:
                hashmap[1].append(nums[i])
        newl=hashmap[0]
        for i in range(len(hashmap[1])):
            newl.append(hashmap[1][i])
        return newl