class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ## use 1st row and 1st  column for marking of the matrix
        n=len(matrix[0])
        m=len(matrix)
        col0=1
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    ## mark the ith row and column matrix
                    matrix[i][0]=0
                    ## mark the jth column
                    if j!=0:
                        matrix[0][j]=0
                    else:
                        col0=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]!=0:
                    if matrix[i][0]==0 or matrix[0][j]==0:
                        matrix[i][j]=0
        ## edge cases
        if matrix[0][0]==0:
            for i in range(n):
                matrix[0][i]=0

        if col0==0:
            for i in range(m):
                matrix[i][0]=0

                   
                
        
        