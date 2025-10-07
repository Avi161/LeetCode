from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp = triangle[-1][:]

        # Work upward from second-to-last row
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

        return dp[0]

Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])