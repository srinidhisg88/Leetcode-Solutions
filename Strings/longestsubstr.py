from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## sliding window technique
        l=0
        maxlen=0
        char_set=set()
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[i])
                l+=1
            char_set.add(s[i])
            maxlen=max(maxlen,i-l+1)
        return maxlen
soln=Solution()
print(soln.lengthOfLongestSubstring('abcaabbc'))
