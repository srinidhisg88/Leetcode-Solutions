class Solution:
    def generateRows(self,n:int)->List[int]:
        an=1
        ansrow=[]
        ansrow.append(an)
        for i in range(1,n):
            an=an*(n-i)
            an=an//i
            ansrow.append(an)
        return ansrow
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(1,numRows+1):
            ans.append(self.generateRows(i))
        return ans
    
