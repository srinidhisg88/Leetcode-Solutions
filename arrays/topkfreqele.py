class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=Counter(nums)
        ## using a method calles most_common()
        l=[]
        for item,value in hashmap.most_common(k):
            l.append(item)
        return l
        
            