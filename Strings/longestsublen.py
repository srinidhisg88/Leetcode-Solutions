class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## sliding window technique
        ## and two pointer approach
        l=0
        n=len(s)
        r=0
        maxlen=0
        length=0
        hashmap=[-1]*256
        while r<n:
            if hashmap[ord(s[r])]!=-1:
                if hashmap[ord(s[r])]>=l:
                    l=hashmap[ord(s[r])]+1
            length=r-l+1
            maxlen=max(length,maxlen)
            hashmap[ord(s[r])]=r
            r+=1
        return maxlen
            
