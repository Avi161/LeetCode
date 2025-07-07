import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for i, num in enumerate(nums):
            if len(minHeap) < k:
                heapq.heappush(minHeap, num)
            else:
                heapq.heappushpop(minHeap, num)
        return minHeap[0]