def find_knapsack(capacity, weights, values, n):
    rows = n
    cols = capacity + 1
    dp = [[0 for i in range(cols)] for j in range(rows)]
    for row in range(rows):
        for col in range(1, cols):
            if weights[row] <= col:
                dp[row][col] = max(dp[row-1][col], dp[row-1][col-weights[row]] + values[row])
            else:
                dp[row][col] = dp[row-1][col]
    return dp[rows-1][capacity]

find_knapsack(capacity=6, weights=[1,2,3,5], values=[1,5,4,8], n=4)

"""
Input:
6 , [1,2,3,5], [1,5,4,8], 4
Output:
10
Expected:
10
"""