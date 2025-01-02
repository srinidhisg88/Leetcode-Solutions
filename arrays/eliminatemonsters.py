class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_to_reach=[dist[i]/speed[i] for i in range(len(dist))]
        time_to_reach.sort()
        for i,time in enumerate(time_to_reach):
            if i>=time:
                return i
        return len(dist)