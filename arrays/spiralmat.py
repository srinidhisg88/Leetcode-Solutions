class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ## identify patterns and layers
        result=[[0]*n for _ in range(n)]
        cnt=1
        for layer in range((n+1)//2):
            # traverse from left to right
            for i in range(layer,n-layer):
                result[layer][i]=cnt
                cnt+=1
            # traverse from top to bottom
            for i in range(layer+1,n-layer):
                result[i][n-layer-1]=cnt
                cnt+=1
            # traverse from right to left
            for i in range(n-layer-2,layer-1,-1):
                result[n-layer-1][i]=cnt
                cnt+=1
            # traverse from bottom to top
            for i in range(n-layer-2,layer,-1):
                result[i][layer]=cnt
                cnt+=1
        return result
            