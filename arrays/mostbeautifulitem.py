class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        ## sort items by price
        items.sort()
        max_beauty=0
        for i in range(len(items)):
            max_beauty=max(max_beauty,items[i][1])
            items[i][1]=max_beauty
        def find_max_beauty(q):
            #binary search to find the max beauty
            low,high=0,len(items)-1
            while low<=high:
                mid=(low+high)//2
                if items[mid][0]<=q:
                    low=mid+1
                else:
                    high=mid-1
            return items[high][1] if high>=0 else 0
        return [find_max_beauty(q) for q in queries]

        

        