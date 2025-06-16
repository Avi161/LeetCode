class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = 0
        num_cnt = defaultdict(int)
        for num in nums:
            num_cnt[num] += 1
        
        cnt_num = []
        heapq.heapify(cnt_num)

        for key, value in num_cnt.items():
            if n < k:
                heapq.heappush(cnt_num, (value, key))
                n += 1
            else:
                heapq.heappushpop(cnt_num, (value, key))
        return [num[1] for num in cnt_num]



