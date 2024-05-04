# Leetcode # 3099. Harshad Number

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x == 100: return 1
        total = x // 10 + x % 10
        return total if x % total == 0 else -1

# beats 92.24% in Runtime, beats 93.64% in Memory Usage