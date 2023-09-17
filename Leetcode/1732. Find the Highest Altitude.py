# Leetcode # 1732. Find the Highest Altitude

from itertools import accumulate
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate([0] + gain))
