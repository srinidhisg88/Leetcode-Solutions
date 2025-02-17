from heapq import heappop, heappush
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the adjacency list
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))  # Directed graph
        
        # Step 2: Initialize time array and priority queue
        time = [float('inf')] * (n + 1)
        time[k] = 0
        pq = [(0, k)]  # Min-Heap: (cost, node)

        # Step 3: Dijkstra’s Algorithm
        while pq:
            curr_time, node = heappop(pq)
            
            for neighbor, travel_time in adj[node]:
                new_time = curr_time + travel_time
                if new_time < time[neighbor]:
                    time[neighbor] = new_time
                    heappush(pq, (new_time, neighbor))

        # Step 4: Get the maximum time among all reachable nodes
        max_time = max(time[1:])  # Ignore index 0 (1-based indexing)
        return max_time if max_time != float('inf') else -1