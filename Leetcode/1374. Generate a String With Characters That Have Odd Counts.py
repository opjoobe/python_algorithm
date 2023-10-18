# Leetcode # 1374. Generate a String With Characters That Have Odd Counts

class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * (n - 1) + ["a", "b"][n % 2 == 0]
        