from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        visit = set()

        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1+w2, n2))
    
        return t if len(visit) == n else -1

Solution().networkDelayTime([[0,1,3], [0,3,2], [0,6,6], [1,2,6], [1,4,1], [2,5,1],[3,1,2],[3,4,3],[4,5,4],[6,5,2]], 7, 0)