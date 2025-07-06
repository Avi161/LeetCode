import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_idx = []
        heapq.heapify(dist_idx)
        for i, p in enumerate(points):
            dist = (p[0]**2+p[1]**2)**0.5
            if len(dist_idx) < k:
                heapq.heappush(dist_idx, (-1*dist, i))
            else:
                heapq.heappushpop(dist_idx, (-1*dist, i))
        return [points[dist_idx[i][1]] for i in range(len(dist_idx))]