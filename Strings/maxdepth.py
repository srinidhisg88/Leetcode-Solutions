class Solution(Object):
    def maxDepth(self,s:str)->int:
        count=0
        maxcnt=0
        for st in s:
            if s=='(':
                count+=1
                if count>maxcnt:
                    maxcnt=count
            if s==')':
                count-=1
        return maxcnt