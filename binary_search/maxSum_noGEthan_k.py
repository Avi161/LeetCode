import bisect
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        maxSum = float("-inf")

        rows, cols = len(matrix), len(matrix[0])

        for top in range(rows):
            col_list = [0]*cols
            for bottom in range(top, rows):
                for i in range(cols):
                    col_list[i] += matrix[bottom][i]

                cur_sum = 0
                prefix_sum = [0]
                for c in col_list:
                    cur_sum += c
                    idx = bisect.bisect_left(prefix_sum, cur_sum-k)
                    if idx < len(prefix_sum):
                        maxSum = max(maxSum, cur_sum-prefix_sum[idx])
                    bisect.insort(prefix_sum, cur_sum)
        return maxSum

Solution().maxSumSubmatrix([[1,0,1],[0,-2,3]], 2)
