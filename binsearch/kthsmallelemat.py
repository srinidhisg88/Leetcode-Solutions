from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l < r:
            mid = (l + r) // 2
            count = 0
            j = n - 1
            
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j + 1)
            
            if count < k:
                l = mid + 1
            else:
                r = mid
        return l