# Leetcode # 70. Climbing Stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0] * (n + 1)
        DP[0], DP[1] = 1, 1
        for i in range(2, n + 1):
            DP[i] = DP[i - 2] + DP[i - 1]
        return DP[n]
      
# 31ms (beats 80.93%)
