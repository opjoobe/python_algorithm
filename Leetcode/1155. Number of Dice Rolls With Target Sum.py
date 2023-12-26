# Leetcode # 1155. Number of Dice Rolls With Target Sum

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        DP = [[0] * (target + 1) for _ in range(n + 1)]
        for j in range(1, min(k, target) + 1):
            DP[1][j] = 1
        for i in range(2, n + 1):
            for j in range(2, target + 1):
                total = 0
                for p in range(1, k + 1):
                    if j - p <= 0:
                        break
                    total += DP[i - 1][j - p]
                DP[i][j] = total % int(1e9 + 7)
        return DP[n][target]
        