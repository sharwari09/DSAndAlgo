# https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]

        # Can also be done in reverse. 
        # Calculate the cost to reach the top of the stairs starting from the top of the stairs.
        '''n = len(cost)
        dp = [0] * (n+2)
        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])'''

"""
Time Complexity: O(n), where n is the number of stairs
Space Complexity: O(n), where n is the number of stairs. 
"""
