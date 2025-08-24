class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k-1+maxPts:
            return 1.0
        
        limit = k - 1 + maxPts
        dp = [0.0]*(limit+1)
        ch = [float(i) for i in range(limit+1)]

        for i in range(k, min(n,limit)+1):
            dp[i] = 1.0
        
        S = max(0, min(n, k-1+maxPts)-k+1)

        for i in range(k-1, -1,-1):
            dp[i] = S/maxPts
            S += dp[i]
            if i + maxPts <= limit:
                S -= dp[i+maxPts]
        return dp[0]

Solution().new21Game(21, 17, 10)