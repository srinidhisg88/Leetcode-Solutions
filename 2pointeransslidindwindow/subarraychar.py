class Solution:
    # this solution describes the no of substrings with the atleast one occurence
    # of a,b and c in the substring
    def numberOfSubstrings(self, s: str) -> int:
        lastseen=[-1]*3
        cnt=0
        for i in range(len(s)):
            lastseen[ord(s[i])-ord('a')]=i
            if lastseen[0]!=-1 and lastseen[1]!=-1 and lastseen[2]!=-1:
                cnt+=(1+min(lastseen))
        return cnt
    