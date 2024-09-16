class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ## same as consecutive 1 problem
        ## we use 2 pointer and sliding window techinque
        l=0
        r=0
        maxlen=0
        maxf=0
        hash=defaultdict(int)
        while r<len(s):
            hash[s[r]]+=1
            maxf=max(maxf,hash[s[r]])
            if (r-l+1)-maxf>k:
                hash[s[l]]-=1
                l+=1
            else:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen