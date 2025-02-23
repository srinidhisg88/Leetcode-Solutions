from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        
        R, C = len(forest), len(forest[0])
        trees = sorted((forest[r][c], r, c) for r in range(R) for c in range(C) if forest[r][c] > 1)
        
        def bfs(sr, sc, tr, tc):
            """Find shortest path from (sr, sc) to (tr, tc) using BFS."""
            queue = deque([(sr, sc, 0)])  # (row, col, steps)
            visited = set()
            visited.add((sr, sc))
            
            while queue:
                r, c, steps = queue.popleft()
                if (r, c) == (tr, tc):
                    return steps
                
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited and forest[nr][nc] > 0:
                        visited.add((nr, nc))
                        queue.append((nr, nc, steps + 1))
            return -1  # Target tree is unreachable
        
        sr, sc = 0, 0  # Start position
        total_steps = 0
        
        for _, tr, tc in trees:
            steps = bfs(sr, sc, tr, tc)
            if steps == -1:
                return -1
            total_steps += steps
            sr, sc = tr, tc  # Move to the tree's position
        
        return total_steps