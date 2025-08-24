from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            curInterval = intervals[i]
            if prevInterval[1] < curInterval[0]:
                res.append(prevInterval)
                prevInterval = curInterval
            else:
                prevInterval = [min(prevInterval[0], curInterval[0]), max(prevInterval[1], curInterval[1])]
        res.append(prevInterval)
        return res

Solution().merge([[1,3],[1,5],[6,7]])