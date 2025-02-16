from queue import PriorityQueue
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        R, C = len(grid), len(grid[0])
        dist = [[float('inf')] * C for _ in range(R)]
        q = PriorityQueue()
        
        dist[0][0] = 1
        q.put((1, 0, 0))  # (distance, row, col)
        
        dirs = [
            (0, 1), (0, -1), (-1, 0), (1, 0), 
            (-1, -1), (1, -1), (-1, 1), (1, 1)
        ]
        
        while not q.empty():
            d, x, y = q.get()
            
            if x == R - 1 and y == C - 1:
                return d  # Found the shortest path
            
            for dx, dy in dirs:
                nr, nc = x + dx, y + dy
                
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                    if dist[nr][nc] > d + 1:
                        dist[nr][nc] = d + 1
                        q.put((d + 1, nr, nc))
        
        return -1