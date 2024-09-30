class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        cnt=0
        
        while cnt!=len(s):
           s=s[1:len(s)]+s[0]
           cnt+=1
           if s==goal:
            return True
        return False 
            