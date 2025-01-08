class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n=len(letters)
        start=0
        end=n-1
        minord=letters[0]
        if target>=letters[-1]:
            return letters[0]
        while start<end:
            mid=(start+end)//2
            if letters[mid]>target:
                end=mid
            else:
                start=mid+1
                
            
        return letters[start]