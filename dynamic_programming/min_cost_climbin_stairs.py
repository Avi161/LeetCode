class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        print(len(cost))
        for i in range(len(cost)-4, -1, -1):
            print(i)
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[1], cost[0])
        
                

