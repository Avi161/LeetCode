import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)
        for num in nums:
            if len(self.heap) < self.k:
                heapq.heappush(self.heap, num)
            else:
                heapq.heappushpop(self.heap, num)


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        
        return self.heap[0]