## using binary search
def func(mid,n,m):
    ans=1
    for _ in range(1,n+1):
        ans*=mid
        if ans>mid:
            return 2
    if ans==mid:
        return 1
    return  0

def binsearch(n,m):
    low=0
    high=m
    while low<=high:
        mid=(low+high)//2
        midN=func(mid,n,m)
        if midN==1:
            return mid
        elif midN==0:
            left=mid+1
        else:
            right=mid-1
    return -1

