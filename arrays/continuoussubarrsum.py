class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ## use dictionary
        hashmap={0:-1}
        prefix=0
        for i,n in enumerate(nums):
            prefix+=n
            r=prefix%k
            if r not in hashmap:
                hashmap[r]=i
            elif i-hashmap[r]>1:
                return True
        return False
