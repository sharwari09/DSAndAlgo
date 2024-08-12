"""
Given a number n, find the nth Catalan number.
https://www.geeksforgeeks.org/program-nth-catalan-number/
"""

def catalan(n):
  if n == 0 or n == 1:
    return 1
  dp = [0] * (n+1)
  dp[0] = 1
  dp[1] = 1

  for i in range(2, n+1): # O(n)
    x = 0 
    y = i - 1
    while x < i and y >= 0: # O(n-1)
      dp[i] += dp[x] * dp[y] # 
      x += 1
      y -= 1
  return dp[-1]

"""
Uisng bottom-up tabulation approach, we can start from the 2nd catalan number to nth. 
Keep on storing every ith Catalan number in the dp array and make use of it to process the further cataln numbers.

Time Complexity: O(n)
Space Complexity: O(n)
"""
