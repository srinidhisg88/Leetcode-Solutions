

class Solution:
    def minimumLength(self, s: str) -> int:
        n=len(s)
        if n<3:
            return n
        hashmap=Counter(s)
        cnt=0
        for value in hashmap.values():
            if value>=3:
                if value%2==0:
                    cnt+=2
                else:
                    cnt+=1
            else:
                cnt+=value
        return cnt