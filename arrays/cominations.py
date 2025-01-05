class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=[]
        newl=[]
        def helper(start):
            if len(newl)==k:
                answer.append(newl[:])
                return
            
            for i in range(start,n+1):
                newl.append(i)
                helper(i+1)
                newl.pop()
        helper(1)
        return answer
            
            
            