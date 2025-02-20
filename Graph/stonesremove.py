from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        maxRow = max(stone[0] for stone in stones)
        maxCol = max(stone[1] for stone in stones)
        
        par = [i for i in range(maxRow + maxCol + 2)]  # Increased by 2 to avoid index issues
        size = [1 for _ in range(maxRow + maxCol + 2)]
        
        def findPar(u):
            if u != par[u]:
                par[u] = findPar(par[u])  # Path compression
            return par[u]
        
        def unionBysize(a, b):
            ulpu = findPar(a)
            ulpv = findPar(b)
            if ulpu == ulpv:
                return
            if size[ulpu] > size[ulpv]:
                par[ulpv] = ulpu
                size[ulpu] += size[ulpv]
            else:
                par[ulpu] = ulpv
                size[ulpv] += size[ulpu]
        
        hashmap = {}
        for i in range(n):
            nodeRow = stones[i][0]
            nodeCol = stones[i][1] + maxRow + 1  # Offset column index to avoid overlap
            unionBysize(nodeRow, nodeCol)
            hashmap[nodeRow] = 1
            hashmap[nodeCol] = 1
        
        cnt = sum(1 for h in hashmap if findPar(h) == h)
        return n - cnt
