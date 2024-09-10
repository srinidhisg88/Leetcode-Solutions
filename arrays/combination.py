class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        n=len(candidates)
        ## using recursion
        def combination(index,target):
            ## base case
            if index==n:
                if target==0:
                    ans.append(ds[:])
                return
            if candidates[index]<=target:
                ds.append(candidates[index])
                
                ## pick 
                combination(index,target-candidates[index])
                ds.pop()
            ## not pick 
            combination(index+1,target)
        combination(0,target)
        return ans
                