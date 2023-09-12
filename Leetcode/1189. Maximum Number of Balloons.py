# Leetcode # 1189. Maximum Number of Balloons

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        resources = collections.Counter(text)
        return min(resources["a"], resources["b"], resources["l"] // 2, resources["o"] // 2, resources["n"])