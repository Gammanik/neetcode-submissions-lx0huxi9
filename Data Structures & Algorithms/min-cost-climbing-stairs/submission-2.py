class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1 for _ in range(len(cost))]

        def dfs(i):
            if i >= len(cost):
                return 0

            if cache[i] == -1:
                cache[i] = cost[i] + min(dfs(i+1), dfs(i+2))

            return cache[i]

        return min(dfs(0), dfs(1))
        
        
    #     n = len(cost)
    #     dp = [0] * n

    #     if n == 1:
    #         return cost[0]
    #     if n == 2:
    #         return min(cost[0], cost[1])

    #     dp[0] = cost[0]
    #     dp[1] = min(cost[0], cost[1])
    #     for i in range(2,n):
    #         dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])

    #     print(dp)
    #     return dp[n-1]

    # def dfs(self, cost: List[int]) -> int:
    #     for i in range(2,n):
    #         dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])


        