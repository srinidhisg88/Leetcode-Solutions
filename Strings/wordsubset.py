class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #using 2 hashmaps and merging them
        count_2=defaultdict(int)
        for w in words2:
            count_w=Counter(w)
            for c,cnt in count_w.items():
                count_2[c]=max(count_2[c],cnt)
        res=[]
        
        for w in words1:
            flag=True
            count_c=Counter(w)
            for c,cnt in count_2.items():
                if count_c[c]<cnt:
                    flag=False
                    break
            if flag:
                res.append(w)
        return res       