import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * w for w in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            num1, num2 = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if num1 != num2:
                heapq.heappush(maxHeap, -1*abs(num1-num2))
        if not maxHeap:
            return 0
        else:
            return -1 * maxHeap[0]