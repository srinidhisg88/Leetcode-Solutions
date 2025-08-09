
# def knapsack(wt,val,W,n):
#     #base case
#     if W==0 or n==0:
#         return 0
#     if t[n][W]!=-1:
#         return t[n][W]
#     ## choice diagram
#     if wt[n-1] <= W:
#         t[n][W] = max(val[n-1] + knapsack(wt, val, W - wt[n-1], n-1), knapsack(wt, val, W, n-1))
#         return t[n][W]
#     else:
#         t[n][W] = knapsack(wt, val, W, n-1)
#         return t[n][W]


##tabulation(top-down)
def knapsack(wt,val,W,n):
    # initialisation
    t=[[0]*(W+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i==0 or j==0:
                t[i][j]=0
    

    for i in range(1,n+1):
        for j in range(1,W+1):
            if wt[i-1]<=j:
                t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][W]
wt=[1,3,4,5]
val=[1,4,5,7]
W=7
n=4
t=[[-1]*(W+1) for _ in range(n+1)]
print(knapsack(wt,val,W,n))

    