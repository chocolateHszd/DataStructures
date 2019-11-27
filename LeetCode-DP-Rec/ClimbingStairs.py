'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''

def climbStairs(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in rage(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
