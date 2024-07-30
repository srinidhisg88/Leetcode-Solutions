'''
rearrange array elements by postive and negative
'''
class Solution:
    def rearrange(self,a):
        pi=0
        ni=1
        res=[]
        for i in range(len(a)):
            if a[i]<0:
                res.insert(ni,a[i])
                ni+=2
            else:
                res.insert(pi,a[i])
                pi+=2
        return res
arr=[3,1,-2,-5,2,-4]
result=Solution()
print(result.rearrange(arr))

