class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        indexS=[0]*200
        indexT=[0]*200
        l=len(s)
        for i in range(l):
            if indexS[ord(s[i])]!=indexT[ord(t[i])]:
                return False
            indexS[ord(s[i])]=i+1
            indexT[ord(t[i])]=i+1
        return True
                