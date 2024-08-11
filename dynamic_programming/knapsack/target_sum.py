# https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        rows = len(nums)
        target_arr = [i for i in range(-1 * total, total +1)]
        cols = (2 * total) + 1
        dp = [[0 for i in range(cols)] for j in range(rows)]
        for col in range(cols):
            if target_arr[col] == (-1 * nums[0]):
                dp[0][col] += 1
            if target_arr[col] == nums[0]:
                dp[0][col] += 1
        hashmap = {}
        for i in range(cols):
            hashmap[target_arr[i]] = i 
        for row in range(1, rows):
            for col in range(cols):
                num = nums[row]
                if (target_arr[col]+num) in hashmap:
                    dp[row][col] += dp[row-1][hashmap[target_arr[col]+num]]
                if (target_arr[col]-num) in hashmap:
                    dp[row][col] += dp[row-1][hashmap[target_arr[col]-num]]
        if target in hashmap:
            return dp[rows-1][hashmap[target]]
        return 0

"""
Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""
