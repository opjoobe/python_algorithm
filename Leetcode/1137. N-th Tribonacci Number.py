class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 3:
            return [0, 1, 1, 2][n]
        dp = [0, 1, 1, 2] + [0] * (n - 3)
        before = dp[3]
        for i in range(4, n + 1):
            before = dp[i] = before * 2 - dp[i - 4]            
        return dp[n]

# 23ms (beats 97.2%)